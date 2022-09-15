from dataclasses import dataclass
from datetime import timedelta
from typing import Union

from dateutil.relativedelta import relativedelta

from src.enums import Currency, TopUpType


@dataclass
class TopUp:
    topup_type: TopUpType
    price: int
    currency: Currency
    duration: Union[timedelta, relativedelta]

    def get_total_cost(self, units: int) -> int:
        return self.price * units

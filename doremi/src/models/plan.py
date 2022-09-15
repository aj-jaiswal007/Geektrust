from dataclasses import dataclass
from datetime import date, timedelta
from typing import Union

from dateutil.relativedelta import relativedelta

from src.constants import RENEWAL_NOTIFY_TIME
from src.enums import Currency, PlanCategory, PlanType


@dataclass
class Plan:
    plan_type: PlanType
    category: PlanCategory
    price: int
    currency: Currency
    duration: Union[timedelta, relativedelta]

    def get_reminder_date(self, start_date: date) -> date:
        return start_date + self.duration - RENEWAL_NOTIFY_TIME

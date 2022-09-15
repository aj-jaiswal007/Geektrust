from typing import Dict

from dateutil.relativedelta import relativedelta

from src.enums import Currency, TopUpType
from src.models import TopUp


# Top ups
TOPUP_FOUR_DEVICE = TopUp(
    topup_type=TopUpType.FOUR_DEVICE,
    price=50,
    currency=Currency.INR,
    duration=relativedelta(months=1),
)
TOPUP_TEN_DEVICE = TopUp(
    topup_type=TopUpType.TEN_DEVICE,
    price=100,
    currency=Currency.INR,
    duration=relativedelta(months=1),
)


# TopUp map for faster looup
TOPUP_MAP: Dict[TopUpType, TopUp] = {
    TopUpType.FOUR_DEVICE: TOPUP_FOUR_DEVICE,
    TopUpType.TEN_DEVICE: TOPUP_TEN_DEVICE,
}

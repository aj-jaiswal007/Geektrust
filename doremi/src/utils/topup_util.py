from src.enums import TopUpType
from src.models import TopUp
from src.resources import TOPUP_MAP


class TopUpUtil:
    ALL_TOPUPS = TOPUP_MAP

    def get_topup(self, topup_type: TopUpType) -> TopUp:
        return self.ALL_TOPUPS[topup_type]

from src.constants import RENEWAL_NOTIFY_TIME
from src.enums import PlanCategory, PlanType
from src.models import Plan
from src.resources import PLAN_MAP


class PlanUtil:
    ALL_PLANS = PLAN_MAP
    RENEWAL_NOTIFY_TIME = RENEWAL_NOTIFY_TIME

    def get_plan(self, category: PlanCategory, plan_type: PlanType) -> Plan:
        return self.ALL_PLANS[category][plan_type]


from enum import Enum


class PlanType(str, Enum):
    FREE = "FREE"
    PERSONAL = "PERSONAL"
    PREMIUM = "PREMIUM"

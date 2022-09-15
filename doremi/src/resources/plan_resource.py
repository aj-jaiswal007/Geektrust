from typing import Dict

from dateutil.relativedelta import relativedelta

from src.enums import Currency, PlanCategory, PlanType
from src.models import Plan

# Music plans
PLAN_MUSIC_FREE = Plan(
    plan_type=PlanType.FREE,
    category=PlanCategory.MUSIC,
    price=0,
    currency=Currency.INR,
    duration=relativedelta(months=1),
)
PLAN_MUSIC_PERSONAL = Plan(
    plan_type=PlanType.PERSONAL,
    category=PlanCategory.MUSIC,
    price=100,
    currency=Currency.INR,
    duration=relativedelta(months=1),
)
PLAN_MUSIC_PREMIUM = Plan(
    plan_type=PlanType.PREMIUM,
    category=PlanCategory.MUSIC,
    price=250,
    currency=Currency.INR,
    duration=relativedelta(months=3),
)


# Video plans
PLAN_VIDEO_FREE = Plan(
    plan_type=PlanType.FREE,
    category=PlanCategory.VIDEO,
    price=0,
    currency=Currency.INR,
    duration=relativedelta(months=1),
)
PLAN_VIDEO_PERSONAL = Plan(
    plan_type=PlanType.PERSONAL,
    category=PlanCategory.VIDEO,
    price=200,
    currency=Currency.INR,
    duration=relativedelta(months=1),
)
PLAN_VIDEO_PREMIUM = Plan(
    plan_type=PlanType.PREMIUM,
    category=PlanCategory.VIDEO,
    price=500,
    currency=Currency.INR,
    duration=relativedelta(months=3),
)

# Podcast plans
PLAN_PODCAST_FREE = Plan(
    plan_type=PlanType.FREE,
    category=PlanCategory.PODCAST,
    price=0,
    currency=Currency.INR,
    duration=relativedelta(months=1),
)
PLAN_PODCAST_PERSONAL = Plan(
    plan_type=PlanType.PERSONAL,
    category=PlanCategory.PODCAST,
    price=100,
    currency=Currency.INR,
    duration=relativedelta(months=1),
)
PLAN_PODCAST_PREMIUM = Plan(
    plan_type=PlanType.PREMIUM,
    category=PlanCategory.PODCAST,
    price=300,
    currency=Currency.INR,
    duration=relativedelta(months=3),
)


# Plan map for faster lookup
PLAN_MAP: Dict[PlanCategory, Dict[PlanType, Plan]] = {
    PlanCategory.MUSIC: {
        PlanType.FREE: PLAN_MUSIC_FREE,
        PlanType.PERSONAL: PLAN_MUSIC_PERSONAL,
        PlanType.PREMIUM: PLAN_MUSIC_PREMIUM,
    },
    PlanCategory.VIDEO: {
        PlanType.FREE: PLAN_VIDEO_FREE,
        PlanType.PERSONAL: PLAN_VIDEO_PERSONAL,
        PlanType.PREMIUM: PLAN_VIDEO_PREMIUM,
    },
    PlanCategory.PODCAST: {
        PlanType.FREE: PLAN_PODCAST_FREE,
        PlanType.PERSONAL: PLAN_PODCAST_PERSONAL,
        PlanType.PREMIUM: PLAN_PODCAST_PREMIUM,
    },
}

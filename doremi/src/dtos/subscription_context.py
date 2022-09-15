from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional
from src.models import Plan, TopUp
from src.enums import PlanCategory


@dataclass
class SubscriptionContext:
    plans: "OrderedDict[PlanCategory, Plan]" = field(default_factory=OrderedDict)
    start_date: Optional[date] = None
    topup: Optional[TopUp] = None
    topup_units: int = 0
    results: List[str] = field(default_factory=list)
    total_amount: int = 0


from src.enums import (ErrorCategory, ErrorReason, PlanCategory,
                       PlanType)
from src.exceptions import InvalidCommandError
from src.dtos import SubscriptionContext
from src.utils import PlanUtil


class AddSubscriptionHandler:

    # dependency
    _plan_util = PlanUtil()

    def __init__(self, context: SubscriptionContext) -> None:
        self.context = context

    def handle(self, category: PlanCategory, plan_type: PlanType):
        """
        - Handles ADD_SUBSCRIPTION command
        - Adds the plan in the context 

        Args:
            category (PlanCategory): Plan Category
            plan_type (PlanType): Plan type

        Raises:
            InvalidCommandError: If start date is invalid or duplicate subcription
        """
        if not self.context.start_date:
            raise InvalidCommandError(
                category=ErrorCategory.ADD_SUBSCRIPTION_FAILED,
                reason=ErrorReason.INVALID_DATE,
            )

        if category in self.context.plans:
            raise InvalidCommandError(
                category=ErrorCategory.ADD_SUBSCRIPTION_FAILED,
                reason=ErrorReason.DUPLICATE_CATEGORY,
            )

        # adding plans to current list
        plan = self._plan_util.get_plan(
            category=category, plan_type=plan_type
        )
        self.context.plans[category] = plan

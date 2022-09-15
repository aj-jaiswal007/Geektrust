
from src.constants import DATE_FORMAT
from src.enums import (ErrorReason, OutputType)
from src.exceptions import InvalidCommandError
from src.dtos import SubscriptionContext


class PrintRenewalDetailsHandler:
    def __init__(self, context: SubscriptionContext) -> None:
        self.context = context

    def handle(self):
        """
        - Handles PRINT_RENEAL_DETAILS command
        - Calculates and sets the renewal details in the context

        Raises:
            InvalidCommandError: If no subscriptions found or start date is invalid
        """

        if not self.context.plans:
            raise InvalidCommandError(
                reason=ErrorReason.SUBSCRIPTIONS_NOT_FOUND)

        assert self.context.start_date, "Start date is not present"
        for plan_category, plan in self.context.plans.items():
            # Adding renewal reminder date
            reminder_date = plan.get_reminder_date(
                start_date=self.context.start_date).strftime(DATE_FORMAT)
            self.context.results.append(
                f"{OutputType.RENEWAL_REMINDER} {plan_category} {reminder_date}")
            # Updating total price
            self.context.total_amount += plan.price

        self.context.results.append(
            f"{OutputType.RENEWAL_AMOUNT} {self.context.total_amount}"
        )

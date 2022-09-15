
from src.enums import ErrorCategory, ErrorReason, TopUpType
from src.exceptions import InvalidCommandError
from src.dtos import SubscriptionContext
from src.utils import TopUpUtil


class AddTopUpHandler:
    # dependency
    _topup_util = TopUpUtil()

    def __init__(self, context: SubscriptionContext) -> None:
        self.context = context

    def handle(self, topup_type: TopUpType, units: int):
        """
        - Handles ADD_TOPUP command
        - Sets the topup details in the context

        Args:
            topup_type (TopUpType): TopUp Type
            units (int): No of topups bought

        Raises:
            InvalidCommandError: If no subscriptions found or duplicate topup
        """
        if not self.context.start_date:
            raise InvalidCommandError(
                category=ErrorCategory.ADD_TOPUP_FAILED,
                reason=ErrorReason.INVALID_DATE,
            )

        if not self.context.plans:
            raise InvalidCommandError(
                category=ErrorCategory.ADD_TOPUP_FAILED,
                reason=ErrorReason.SUBSCRIPTIONS_NOT_FOUND,
            )

        if self.context.topup:
            raise InvalidCommandError(
                category=ErrorCategory.ADD_TOPUP_FAILED,
                reason=ErrorReason.DUPLICATE_TOPUP,
            )

        topup = self._topup_util.get_topup(topup_type=topup_type)
        self.context.topup = topup
        self.context.topup_units = units
        self.context.total_amount += topup.get_total_cost(units=units)

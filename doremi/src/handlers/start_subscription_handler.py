from datetime import datetime

from src.constants import DATE_FORMAT
from src.enums import ErrorReason
from src.exceptions import InvalidCommandError
from src.dtos import SubscriptionContext


class StartSubscriptionHandler:
    def __init__(self, context: SubscriptionContext) -> None:
        self.context = context

    def handle(self, start_date: str):
        """
        - Handles START_SUBSCRIPTION command
        - Sets the start_date in the context

        Args:
            start_date (str): start date in format DD-MM-YYYY

        Raises:
            InvalidCommandError: If date is invalid
        """
        try:
            self.context.start_date = datetime.strptime(
                start_date, DATE_FORMAT).date()
        except ValueError:
            raise InvalidCommandError(reason=ErrorReason.INVALID_DATE)

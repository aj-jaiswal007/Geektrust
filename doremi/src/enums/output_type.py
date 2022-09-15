from enum import Enum


class OutputType(str, Enum):
    RENEWAL_REMINDER = "RENEWAL_REMINDER"
    RENEWAL_AMOUNT = "RENEWAL_AMOUNT"

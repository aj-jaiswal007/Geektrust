from enum import Enum


class InputCommand(str, Enum):
    START_SUBSCRIPTION = "START_SUBSCRIPTION"
    ADD_SUBSCRIPTION = "ADD_SUBSCRIPTION"
    ADD_TOPUP = "ADD_TOPUP"
    PRINT_RENEWAL_DETAILS = "PRINT_RENEWAL_DETAILS"
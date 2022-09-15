from enum import Enum


class ErrorCategory(str, Enum):
    ADD_SUBSCRIPTION_FAILED = "ADD_SUBSCRIPTION_FAILED"
    ADD_TOPUP_FAILED = "ADD_TOPUP_FAILED"

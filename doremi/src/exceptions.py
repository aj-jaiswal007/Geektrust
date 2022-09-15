from typing import Optional

from src.enums import ErrorCategory, ErrorReason


class InvalidCommandError(Exception):
    def __init__(
        self,
        category: Optional[ErrorCategory] = None,
        reason: Optional[ErrorReason] = None,
    ):
        self.category = category or ""
        self.reason = reason or ""

    def __str__(self) -> str:
        return f"{self.category} {self.reason}".strip()

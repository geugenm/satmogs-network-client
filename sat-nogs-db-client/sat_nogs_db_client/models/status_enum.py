from enum import Enum


class StatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ObservationsListVettedStatus(str, Enum):
    BAD = "bad"
    FAILED = "failed"
    GOOD = "good"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)

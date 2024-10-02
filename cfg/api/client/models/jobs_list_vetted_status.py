from enum import Enum


class JobsListVettedStatus(str, Enum):
    BAD = "bad"
    FAILED = "failed"
    GOOD = "good"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)

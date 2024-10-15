from enum import Enum


class TleListFormat(str, Enum):
    JSON = "json"
    VALUE_0 = "3le"

    def __str__(self) -> str:
        return str(self.value)

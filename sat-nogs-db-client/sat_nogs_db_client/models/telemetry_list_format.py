from enum import Enum


class TelemetryListFormat(str, Enum):
    JSON = "json"
    JSON_LD = "json-ld"

    def __str__(self) -> str:
        return str(self.value)

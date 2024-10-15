from enum import Enum


class IaruCoordinationEnum(str, Enum):
    IARU_COORDINATED = "IARU Coordinated"
    IARU_DECLINED = "IARU Declined"
    IARU_UNCOORDINATED = "IARU Uncoordinated"
    NA = "N/A"

    def __str__(self) -> str:
        return str(self.value)

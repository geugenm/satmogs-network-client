from enum import Enum


class TypeEnum(str, Enum):
    TRANSCEIVER = "Transceiver"
    TRANSMITTER = "Transmitter"
    TRANSPONDER = "Transponder"

    def __str__(self) -> str:
        return str(self.value)

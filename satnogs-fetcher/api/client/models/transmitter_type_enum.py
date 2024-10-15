from enum import Enum


class TransmitterTypeEnum(str, Enum):
    TRANSCEIVER = "Transceiver"
    TRANSMITTER = "Transmitter"
    TRANSPONDER = "Transponder"

    def __str__(self) -> str:
        return str(self.value)

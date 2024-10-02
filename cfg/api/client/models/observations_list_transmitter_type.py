from enum import Enum


class ObservationsListTransmitterType(str, Enum):
    TRANSCEIVER = "Transceiver"
    TRANSMITTER = "Transmitter"
    TRANSPONDER = "Transponder"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ServiceEnum(str, Enum):
    AERONAUTICAL = "Aeronautical"
    AMATEUR = "Amateur"
    BROADCASTING = "Broadcasting"
    EARTH_EXPLORATION = "Earth Exploration"
    FIXED = "Fixed"
    INTER_SATELLITE = "Inter-satellite"
    MARITIME = "Maritime"
    METEOROLOGICAL = "Meteorological"
    MOBILE = "Mobile"
    RADIOLOCATION = "Radiolocation"
    RADIONAVIGATIONAL = "Radionavigational"
    SPACE_OPERATION = "Space Operation"
    SPACE_RESEARCH = "Space Research"
    STANDARD_FREQUENCY_AND_TIME_SIGNAL = "Standard Frequency and Time Signal"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

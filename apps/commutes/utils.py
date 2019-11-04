from enum import IntEnum


class CommuteUsageTypes(IntEnum):
    TO_WORK = 1
    MEETING = 2
    OTHER = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

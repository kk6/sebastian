import datetime
from enum import IntEnum
from typing import List


class CommuteUsageTypes(IntEnum):
    TO_WORK = 1
    MEETING = 2
    OTHER = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


def dates_str_to_dates(dates: str, separator=",") -> List[datetime.date]:
    """区切り文字で連続入力された日付文字列をdateのリストにして返す"""
    return [
        datetime.datetime.strptime(d, "%Y/%m/%d").date() for d in dates.split(separator)
    ]

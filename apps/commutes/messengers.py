from dataclasses import asdict
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import List
from typing import Optional

from .utils import CommuteUsageTypes


@dataclass
class CommuteRegisterInputDto:
    usage_type: CommuteUsageTypes
    usage_text: Optional[str]
    departure_station: Optional[str]
    arrival_station: Optional[str]
    date_of_use: List[date]
    price: Decimal
    is_round_trip: bool
    has_apply: bool
    user_id: int

    def to_dict(self):
        d = asdict(self)
        d.pop("is_round_trip")
        return d

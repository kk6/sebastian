from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import List
from typing import Optional

from .utils import CommuteUsageTypes


@dataclass
class CommuteDto:
    usage_type: CommuteUsageTypes
    usage_text: Optional[str]
    departure_station: str
    arrival_station: str
    price: Decimal
    date_of_use: date
    has_apply: bool
    user_id: int


@dataclass
class CommuteRegisterInputDto:
    commutes: List[CommuteDto]

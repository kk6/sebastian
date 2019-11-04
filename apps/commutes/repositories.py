from typing import Optional
from typing import TYPE_CHECKING

from .models import Commute

if TYPE_CHECKING:
    from django.conf import settings
    from datetime import date
    from .utils import CommuteUsageTypes


class CommuteRepository:
    """交通費のリポジトリ"""

    def __init__(self, model_commute=Commute):
        self.model_commute = model_commute

    def create_commute(
        self,
        usage_type: CommuteUsageTypes,
        usage_text: Optional[str],
        departure_station: str,
        arrival_station: str,
        price: int,
        date_of_use: "date",
        has_apply: bool,
        user: "settings.AUTH_USER_MODEL",
    ) -> Commute:
        """交通費を作成する"""
        commute = self.model_commute(
            usage_type=usage_type,
            usage_text=usage_text,
            departure_station=departure_station,
            arrival_station=arrival_station,
            price=price,
            date_of_use=date_of_use,
            has_apply=has_apply,
            user=user,
        )
        commute.save()
        return commute

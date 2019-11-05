import typing

from .models import Commute
from .utils import CommuteUsageTypes

if typing.TYPE_CHECKING:
    from django.conf import settings
    from datetime import date


class RoundTripCommuteCreationInteractor:
    def __init__(self, commute_repo):
        self.commute_repo = commute_repo
        self._up_line_params = None
        self._down_line_params = None

    def set_params(
        self,
        usage_type: CommuteUsageTypes,
        usage_text: typing.Optional[str],
        price: int,
        departure_station: str,
        arrival_station: str,
        has_apply: bool,
        date_of_use: "date",
        user: "settings.AUTH_USER_MODEL",
    ):
        self._up_line_params = dict(
            usage_type=usage_type,
            usage_text=usage_text,
            price=price,
            departure_station=departure_station,
            arrival_station=arrival_station,
            has_apply=has_apply,
            date_of_use=date_of_use,
            user=user,
        )
        d = self._up_line_params.copy()
        d["departure_station"], d["arrival_station"] = (
            d["arrival_station"],
            d["departure_station"],
        )
        self._down_line_params = d

    def execute(self) -> typing.Tuple[Commute, Commute]:
        up_line_commute = self.commute_repo.create_commute(**self._up_line_params)
        down_line_commute = self.commute_repo.create_commute(**self._down_line_params)
        return up_line_commute, down_line_commute

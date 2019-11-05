import typing

from .utils import CommuteUsageTypes
from .utils import dates_str_to_dates

if typing.TYPE_CHECKING:
    from django.conf import settings
    from datetime import date
    from .models import Commute


class CommuteApp:
    """交通費のアプリケーションモデル"""

    def __init__(self, commute_repo):
        self.commute_repo = commute_repo

    def create_commute(
        self,
        usage_type: CommuteUsageTypes,
        usage_text: typing.Optional[str],
        price: int,
        departure_station: str,
        arrival_station: str,
        has_apply: bool,
        date_of_use: "date",
        user: "settings.AUTH_USER_MODEL",
    ) -> "Commute":
        """交通費記録を作成する"""
        commute = self.commute_repo.create_commute(
            usage_type=usage_type,
            usage_text=usage_text,
            departure_station=departure_station,
            arrival_station=arrival_station,
            price=price,
            date_of_use=date_of_use,
            has_apply=has_apply,
            user=user,
        )
        return commute

    def create_commute_by_form(
        self,
        usage_type: str,
        usage_text: typing.Optional[str],
        price: int,
        route: str,
        departure_station: str,
        arrival_station: str,
        is_round_trip: bool,
        has_apply: bool,
        date_of_use: str,
        user: "settings.AUTH_USER_MODEL",
    ) -> None:
        """フォームデータを加工しつつ交通費記録を作成する"""
        _usage_type = CommuteUsageTypes(int(usage_type))
        departure_station, arrival_station = complete_stations(
            route, departure_station, arrival_station
        )
        dates_of_use = dates_str_to_dates(date_of_use)
        for _date_of_use in dates_of_use:
            self.create_commute(
                usage_type=_usage_type,
                usage_text=usage_text,
                departure_station=departure_station,
                arrival_station=arrival_station,
                price=price,
                date_of_use=_date_of_use,
                has_apply=has_apply,
                user=user,
            )
            if is_round_trip:
                self.create_commute(
                    usage_type=_usage_type,
                    usage_text=usage_text,
                    departure_station=departure_station,
                    arrival_station=arrival_station,
                    price=price,
                    date_of_use=_date_of_use,
                    has_apply=has_apply,
                    user=user,
                )


def complete_stations(
    route_type: str,
    departure_station: typing.Optional[str],
    arrival_station: typing.Optional[str],
):
    """経路が「自宅〜会社」の時に駅名を補完する"""
    # TODO: ユーザーのデフォルト経路を登録できるようにしてそれを入れるように直す
    if route_type == "1":
        departure_station = "椎名町駅"
        arrival_station = "新宿駅"
    return departure_station, arrival_station

import typing

from .utils import CommuteUsageTypes
from .utils import dates_str_to_dates

if typing.TYPE_CHECKING:
    from django.conf import settings


class CommuteApp:
    """交通費のアプリケーションモデル"""

    def __init__(self, commute_repo):
        self.commute_repo = commute_repo

    def create_commute(self, data: dict, user: "settings.AUTH_USER_MODEL") -> None:
        """交通費記録を作成する"""
        usage_type = CommuteUsageTypes(int(data.get("usage_type")))
        price = data.get("price")
        route_type = data.get("route")
        departure_station = data.get("departure_station")
        arrival_station = data.get("arrival_station")
        departure_station, arrival_station = complete_stations(
            route_type, departure_station, arrival_station
        )
        is_round_trip = data.get("is_round_trip")
        has_apply = data.get("has_apply")
        dates = dates_str_to_dates(data.get("date_of_use"))
        for date in dates:
            self.commute_repo.create_commute(
                usage_type=usage_type,
                departure_station=departure_station,
                arrival_station=arrival_station,
                price=price,
                date_of_use=date,
                has_apply=has_apply,
                user=user,
            )
            if is_round_trip:
                self.commute_repo.create_commute(
                    usage_type=usage_type,
                    departure_station=arrival_station,
                    arrival_station=departure_station,
                    price=price,
                    date_of_use=date,
                    has_apply=has_apply,
                    user=user,
                )


def complete_stations(route_type, departure_station, arrival_station):
    """経路が「自宅〜会社」の時に駅名を補完する"""
    # TODO: ユーザーのデフォルト経路を登録できるようにしてそれを入れるように直す
    if route_type == "1":
        departure_station = "椎名町駅"
        arrival_station = "新宿駅"
    return departure_station, arrival_station

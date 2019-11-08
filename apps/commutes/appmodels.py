import dataclasses
import typing

from .messengers import CommuteRegisterInputDto


class CommuteApp:
    """交通費のアプリケーションモデル"""

    def __init__(self, commute_repo):
        self.commute_repo = commute_repo

    def create_commute_by_register_form(
        self, input_dto: CommuteRegisterInputDto
    ) -> None:
        """フォームより交通費記録を作成する"""
        for commute_dto in input_dto.commutes:
            self.commute_repo.create_commute(**dataclasses.asdict(commute_dto))


def complete_stations(
    route_type: int,
    departure_station: typing.Optional[str],
    arrival_station: typing.Optional[str],
):
    """経路が「自宅〜会社」の時に駅名を補完する"""
    # TODO: ユーザーのデフォルト経路を登録できるようにしてそれを入れるように直す
    if route_type == 1:
        departure_station = "椎名町駅"
        arrival_station = "新宿駅"
    return departure_station, arrival_station

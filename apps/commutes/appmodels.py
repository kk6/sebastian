import typing

from .interactors import RoundTripCommuteCreationInteractor
from .messengers import CommuteRegisterInputDto

if typing.TYPE_CHECKING:
    from .models import Commute


class CommuteApp:
    """交通費のアプリケーションモデル"""

    def __init__(self, commute_repo):
        self.commute_repo = commute_repo

    def create_commute(self, input_dto: CommuteRegisterInputDto) -> "Commute":
        """交通費記録（片道）を作成する"""
        commute = self.commute_repo.create_commute_multiple(**input_dto.to_dict())
        return commute

    def create_round_trip_commute(
        self, input_dto: CommuteRegisterInputDto
    ) -> typing.Tuple["Commute", "Commute"]:
        """往復の交通費を作成する"""
        interactor = RoundTripCommuteCreationInteractor(self.commute_repo)
        interactor.set_params(input_dto)
        return interactor.execute()

    def create_commute_by_register_form(
        self, input_dto: CommuteRegisterInputDto
    ) -> None:
        """フォームより交通費記録を作成する"""
        # FIXME: repoに渡す引数はformの知識を持つべきではない気がする。
        #        input_dtoを持ち込むのはユースケースまでに留めるべき。
        if input_dto.is_round_trip:
            self.create_round_trip_commute(input_dto)
        else:
            self.create_commute(input_dto)


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

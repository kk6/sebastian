import typing

from .messengers import CommuteRegisterInputDto
from .models import Commute


class RoundTripCommuteCreationInteractor:
    def __init__(self, commute_repo):
        self.commute_repo = commute_repo
        self._up_line_params = None
        self._down_line_params = None

    def set_params(self, input_dto: CommuteRegisterInputDto):
        self._up_line_params = input_dto.to_dict()
        c = self._up_line_params.copy()
        c["departure_station"], c["arrival_station"] = (
            c["arrival_station"],
            c["departure_station"],
        )
        self._down_line_params = c

    def execute(self) -> typing.Tuple[Commute, Commute]:
        up_line_commute = self.commute_repo.create_commute_multiple(
            **self._up_line_params
        )
        down_line_commute = self.commute_repo.create_commute_multiple(
            **self._down_line_params
        )
        return up_line_commute, down_line_commute

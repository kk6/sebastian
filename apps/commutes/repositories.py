from .models import Commute


class CommuteRepository:
    """交通費のリポジトリ"""

    def __init__(self, model_commute=Commute):
        self.model_commute = model_commute

    def create_commute(
        self,
        usage_type,
        usage_text,
        departure_station,
        arrival_station,
        price,
        date_of_use,
        has_apply,
        user,
    ):
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

from django.contrib.auth import get_user_model
from django.db import models

from .utils import CommuteUsageTypes

User = get_user_model()


class Commute(models.Model):
    """交通費"""

    usage_type = models.IntegerField(
        "利用種別", choices=CommuteUsageTypes.choices(), default=CommuteUsageTypes.TO_WORK
    )
    departure_station = models.CharField("出発駅", max_length=255)
    arrival_station = models.CharField("到着駅", max_length=255)
    price = models.DecimalField("金額", max_digits=10, decimal_places=2)
    date_of_use = models.DateField("利用日")
    has_apply = models.BooleanField("申請済み", default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_commute_usage_type_label(self):
        return CommuteUsageTypes(self.usage_type).name.title()

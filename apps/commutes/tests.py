import datetime

from django.test import TestCase
from users.factories import UserFactory


class CommuteTests(TestCase):
    def _get_app(self):
        from .appmodels import CommuteApp
        from .repositories import CommuteRepository

        return CommuteApp(CommuteRepository())

    def test_it(self):
        from .utils import CommuteUsageTypes

        app = self._get_app()
        today = datetime.date.today()
        user = UserFactory()
        obj = app.create_commute(
            usage_type=CommuteUsageTypes.MEETING,
            usage_text="",
            departure_station="椎名町駅",
            arrival_station="JR新宿駅",
            price=304,
            date_of_use=today,
            has_apply=True,
            user=user,
        )
        self.assertEqual(obj.usage_type, CommuteUsageTypes.MEETING)
        self.assertEqual(obj.usage_text, None)
        self.assertEqual(obj.departure_station, "椎名町駅")
        self.assertEqual(obj.arrival_station, "JR新宿駅")
        self.assertEqual(obj.price, 304)
        self.assertEqual(obj.date_of_use, today)
        self.assertEqual(obj.has_apply, True)
        self.assertEqual(obj.user, user)

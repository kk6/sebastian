import datetime

from django.test import TestCase
from users.factories import UserFactory


class CommuteTests(TestCase):
    def test_it(self):
        from .models import Commute
        from .utils import CommuteUsageTypes

        today = datetime.date.today()
        obj = Commute.objects.create(
            usage_type=CommuteUsageTypes.MEETING,
            departure_station="椎名町駅",
            arrival_station="JR新宿駅",
            price=304,
            date_of_use=today,
            user=UserFactory(),
        )
        self.assertEqual(obj.usage_type, CommuteUsageTypes.MEETING)
        self.assertEqual(obj.departure_station, "椎名町駅")
        self.assertEqual(obj.arrival_station, "JR新宿駅")
        self.assertEqual(obj.price, 304)
        self.assertEqual(obj.date_of_use, today)

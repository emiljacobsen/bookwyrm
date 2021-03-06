import json
import pathlib
from django.test import TestCase

from bookwyrm import activitypub, models


class Person(TestCase):
    def setUp(self):
        self.user = models.User.objects.create_user(
            'rat', 'rat@rat.com', 'ratword',
        )
        datafile = pathlib.Path(__file__).parent.joinpath(
            '../data/ap_user.json'
        )
        self.user_data = json.loads(datafile.read_bytes())


    def test_load_user_data(self):
        activity = activitypub.Person(**self.user_data)
        self.assertEqual(activity.id, 'https://example.com/user/mouse')
        self.assertEqual(activity.preferredUsername, 'mouse')
        self.assertEqual(activity.type, 'Person')

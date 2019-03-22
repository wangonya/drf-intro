from rest_framework.test import APITestCase, APIClient
from .models import Team

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_teammate(name=""):
        if name != "":
            Team.objects.create(name=name)

    def setUp(self):
        # add test data
        self.create_song("Jonathan")
        self.create_song("Wekesa")
        self.create_song("Bidan")
        self.create_song("Wanjala")
        self.create_song("Philo")

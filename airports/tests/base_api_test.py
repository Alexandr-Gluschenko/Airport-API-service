from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


class BaseAirportAPITest(APITestCase):
    payload = None
    url = None

    def setUp(self):
        if self.url is None:
            self.skipTest("Base test class")

        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.com",
            password="password123",
            is_staff=True,
            is_superuser=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.post(self.url, self.payload)
        self.assertEqual(response.status_code, 201)

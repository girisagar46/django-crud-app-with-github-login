from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from crudapp.constants import TEST_PASSWORD, TEST_USER

from .views import AddView, IndexView


class ViewTest(TestCase):
    def setUp(self):
        self.test_url_names = [
            {
                "url": "personalprofile:index",
                "expected": "/",
                "view": IndexView,
            },
            {
                "url": "personalprofile:add",
                "expected": "/add/",
                "view": AddView,
            },
        ]
        self.client = Client()
        self.user = self.client.login(username=TEST_USER, password=TEST_PASSWORD)

    def test_urls(self):
        for test_url in self.test_url_names:
            with self.subTest(test_url=test_url["url"]):
                url = reverse(test_url["url"])
                self.assertEqual(url, test_url["expected"])

    def test_get(self):
        for test_url in self.test_url_names:
            with self.subTest(test_url=test_url["url"]):
                request = RequestFactory().get(test_url["url"])
                request.user = self.user
                response = test_url["view"].as_view()(request)
                self.assertEquals(response.status_code, 200)

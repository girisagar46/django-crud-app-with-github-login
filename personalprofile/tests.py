from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from crudapp.constants import TEST_PASSWORD, TEST_USER

from .views import IndexView


class IndexViewTest(TestCase):
    def test_urls(self):
        url = reverse("personalprofile:index")
        self.assertEqual(url, "/")

    def test_get(self):
        client = Client()
        user = client.login(username=TEST_USER, password=TEST_PASSWORD)

        request = RequestFactory().get("/")
        request.user = user
        response = IndexView.as_view()(request)
        self.assertEquals(response.status_code, 200)

from django.urls import reverse

from .views import AddView, AllProfilesView, DeleteView, EditView, IndexView, InfoView

TEST_USER = "testuser"
TEST_PASSWORD = "hogehoge"

TEST_VIEWS_LIST = [
    {
        "url": reverse("personalprofile:index"),
        "expected": "/",
        "view": IndexView,
    },
    {
        "url": reverse("personalprofile:add"),
        "expected": "/add/",
        "view": AddView,
    },
    {
        "url": reverse("personalprofile:edit", kwargs={"pk": 1}),
        "expected": "/edit/1/",
        "view": EditView,
    },
    {
        "url": reverse("personalprofile:delete", kwargs={"pk": 1}),
        "expected": "/delete/1/",
        "view": DeleteView,
    },
    {
        "url": reverse("personalprofile:profiles"),
        "expected": "/profiles/",
        "view": AllProfilesView,
    },
    {
        "url": reverse("personalprofile:info", kwargs={"pk": 1}),
        "expected": "/info/1/",
        "view": InfoView,
    },
]

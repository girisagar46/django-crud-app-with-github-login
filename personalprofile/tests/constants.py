from django.urls import reverse

from personalprofile.views import DeleteView, EditView, IndexView

TEST_USER = "testuser"
TEST_PASSWORD = "hogehoge"

TEST_VIEWS_LIST = [
    {
        "url": reverse("personalprofile:index"),
        "expected": "/",
        "view": IndexView,
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
]

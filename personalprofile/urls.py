from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "personalprofile"

urlpatterns = [
    path(
        "",
        login_required(views.IndexView.as_view(), login_url="/login/"),
        name="index",
    ),
    path(
        "accounts/profile/",
        login_required(views.IndexView.as_view(), login_url="/login/"),
        name="profile",
    ),
    path("add/", login_required(views.AddView.as_view(), login_url="/login/"), name="add"),
    path(
        "profiles/",
        login_required(views.AllProfilesView.as_view(), login_url="/login/"),
        name="profiles",
    ),
    path(
        "info/<int:pk>/",
        login_required(views.InfoView.as_view(), login_url="/login/"),
        name="info",
    ),
    path(
        "edit/<int:pk>/",
        login_required(views.EditView.as_view(), login_url="/login/"),
        name="edit",
    ),
    path(
        "delete/<int:pk>/",
        login_required(views.DeleteView.as_view(), login_url="/login/"),
        name="delete",
    ),
]

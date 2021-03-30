import json

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import PersonalProfile
from .utils import get_github_profile


class IndexView(generic.ListView):
    model = PersonalProfile
    template_name = "index.html"


class AddView(generic.CreateView):
    model = PersonalProfile
    fields = ["name"]
    template_name = "add.html"
    fields = "__all__"
    success_url = reverse_lazy("personalprofile:index")

    def get(self, request, *args, **kwargs):
        username = self.request.user
        profile = get_github_profile(username=username)
        self.initial = {
            "username": username,
            "fullname": profile.get("name"),
            "description": profile.get("bio"),
            "email": profile.get("email"),
            "additional_info": json.dumps(profile, indent=4),
        }
        return super().get(request, *args, **kwargs)


class EditView(generic.UpdateView):
    model = PersonalProfile
    fields = ["name", "pk"]
    template_name = "edit.html"
    fields = "__all__"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("personalprofile:index")


class DeleteView(generic.DeleteView):
    model = PersonalProfile
    template_name = "confirm-delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("personalprofile:index")

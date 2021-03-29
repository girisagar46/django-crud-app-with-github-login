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

    def get_queryset(self):
        """Overrides the default ListView to update or create GitHub profile record."""
        username = self.request.user
        profile = get_github_profile(username=username)
        # Saves the basic info from GitHub API
        self.model.objects.update_or_create(
            username=username, fullname=profile.get("name"), description=profile.get("bio")
        )

    def get_context_data(self, **kwargs):
        context = self.model.objects.filter(username=self.request.user)
        return {"profile": context}


class AddView(generic.CreateView):
    model = PersonalProfile
    fields = ["name"]
    template_name = "add.html"
    fields = "__all__"
    success_url = reverse_lazy("personalprofile:profiles")


class EditView(generic.UpdateView):
    model = PersonalProfile
    fields = ["name", "pk"]
    template_name = "edit.html"
    fields = "__all__"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("personalprofile:profiles")


class DeleteView(generic.DeleteView):
    model = PersonalProfile
    template_name = "confirm-delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("personalprofile:profiles")


class AllProfilesView(generic.ListView):
    model = PersonalProfile
    template_name = "profiles.html"
    context_object_name = "post_list"


class InfoView(generic.DetailView):
    model = PersonalProfile
    template_name = "info.html"
    context_object_name = "personalprofile"

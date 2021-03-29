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
        self.model.objects.update_or_create(
            username=username,
            fullname=profile.get("name"),
            description=profile.get("bio"),
            additional_info=json.dumps(profile, indent=4),
        )

    def get_context_data(self, **kwargs):
        context = self.model.objects.filter(username=self.request.user)
        return {"profile": context}


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

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import PersonalProfile


@login_required(login_url="/login/")
def home(request):
    return render(request, "index.html")


class IndexView(generic.ListView):
    model = PersonalProfile
    template_name = "index.html"


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
    success_url = reverse_lazy("personalprofile:index")


class DeleteView(generic.DeleteView):
    model = PersonalProfile
    template_name = "confirm-delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("personalprofile:index")


class AllProfilesView(generic.ListView):
    model = PersonalProfile
    template_name = "profiles.html"
    context_object_name = "post_list"


class InfoView(generic.DetailView):
    model = PersonalProfile
    template_name = "info.html"
    context_object_name = "personalprofile"

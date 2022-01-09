from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView
from django.views.generic.edit import CreateView
from groups.models import Group, GroupMember


class CreateGroup(LoginRequiredMixin, CreateView):
    model = Group
    fields = ["name", "description"]


class SingleGroup(DetailView):
    model = Group
    # slug_url_kwarg = "single_slug"


class ListGroups(ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, RedirectView):
    # slug_url_kwarg = "join_slug"

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, "Warning! Already a member")
        else:
            messages.success(self.request, "You are now a member!")

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(
                user=self.request.user, group__slug=self.kwargs.get("slug")
            ).get()

        except GroupMember.DoesNotExist:
            messages.warning(self.request, "You can't leave this group because you aren't in it.")

        else:
            membership.delete()
            messages.success(self.request, "You have successfully left this group.")
        return super().get(request, *args, **kwargs)

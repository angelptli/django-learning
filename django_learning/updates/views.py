from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
from .forms import UpdateCreateForm
from .models import OwnerUpdate


class UpdateCreateView(CreateView):

    """Display a list of updates."""

    template_name = 'updates/ownerupdate_create.html'
    form_class = UpdateCreateForm
    queryset = OwnerUpdate.objects.all()

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)


class UpdateListView(ListView):

    """Display a list of updates."""

    template_name = 'updates/ownerupdate_list.html'
    queryset = OwnerUpdate.objects.all()


class UpdateDetailView(DetailView):

    """Show the details of the each update."""

    template_name = 'updates/ownerupdate_detail.html'
    queryset = OwnerUpdate.objects.all()

    def get_object(self):
        """Override keyword argument to change the url to id. The default
        keyword for this view is pk."""
        id = self.kwargs.get("id")
        return get_object_or_404(OwnerUpdate, id=id)
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
from .models import OwnerUpdate


class UpdateListView(ListView):
    template_name = 'updates/ownerupdate_list.html'
    queryset = OwnerUpdate.objects.all()
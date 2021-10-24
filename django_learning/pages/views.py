from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # renders the request being made and specify the home template
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return HttpResponse(request, "contact.html", {})


def items_view(request, *args, **kwargs):
    return HttpResponse(request, "items.html", {})


def contribute_view(request, *args, **kwargs):
    return HttpResponse(request, "contribute.html", {})
from django.http import HttpResponse
from django.shortcuts import render


def home_view(*args, **kwargs):
    # request.user requests and identifies the user
    return HttpResponse("<h1>Welcome!</h1>")


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Us</h1>")


def items_view(*args, **kwargs):
    return HttpResponse("<h1>Dim Sum</h1>")


def contribute_view(*args, **kwargs):
    return HttpResponse("<h1>Contribute to our dim sum collection</h1>")
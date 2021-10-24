from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    # renders the request being made and specify the home template
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def items_view(request, *args, **kwargs):
    my_context = {
        "dimsum_list": ["shumai", "sonton"]
    }
    return render(request, "items.html", my_context)


def contribute_view(request, *args, **kwargs):
    my_context = {
        "contributed": "Yes",
        "num_items": 111
    }
    return render(request, "contribute.html", my_context)
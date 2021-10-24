from django.http import HttpResponse
from django.shortcuts import render
from dim_sum.models import DimSumItem

def home_view(request, *args, **kwargs):
    # renders the request being made and specify the home template
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def items_view(request, *args, **kwargs):
    queryset = DimSumItem.objects.all()

    return render(request, "items.html", {'queryset': queryset})


def contribute_view(request, *args, **kwargs):
    my_context = {
        "contributed": "Yes",
        "num_items": 111,
        "contributions": [2, 4, 10, 16, 20, 34]
    }
    return render(request, "contribute.html", my_context)
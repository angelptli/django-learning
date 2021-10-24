from django.shortcuts import render
from .models import DimSumItem


def dimsum_detail_view(request):
    items = DimSumItem.objects.all()

    return render(request, "dim_sum/detail.html", {'items': items})
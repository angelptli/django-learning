from django.shortcuts import render
from .models import DimSumItem
from .forms import AddItemForm


def dimsum_detail_view(request):
    items = DimSumItem.objects.all()

    return render(request, "dim_sum/detail.html", {'items': items})


def add_item_view(request):
    form = AddItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        # Clear out form
        form = AddItemForm()

    context = {
        'form': form
    }

    return render(request, "dim_sum/add_item.html", context)
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import DimSumItem
from .forms import AddItemForm, RawItemForm


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
        "form": form
    }

    return render(request, "dim_sum/add_item.html", context)


# def add_item_view(request):
#     form = RawItemForm()

#     if request.method == "POST":
#         form = RawItemForm(request.POST)
#         if form.is_valid():
#             DimSumItem.objects.create(**form.cleaned_data)

#     context = {'form': form}

#     return render(request, "dim_sum/add_item.html", context)


def render_initial_data(request):
    initial_data = {
        "description": "Best dim sum ever!",
    }

    obj = DimSumItem.objects.get(id=1)
    form = RawItemForm(request.POST or None, initial=initial_data, instance=obj)

    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, "dim_sum/add_item.html", context)


def dimsum_lookup_view(request, id):
    # obj = DimSumItem.objects.get(id=id)
    # obj = get_object_or_404(DimSumItem, id=id)
    try:
        obj = DimSumItem.objects.get(id=id)
    except DimSumItem.DoesNotExist:
        raise Http404

    context = {
        "object": obj
    }

    return render(request, "dim_sum/dimsum_lookup.html", context)


def item_delete_view(request, id):
    obj = get_object_or_404(DimSumItem, id=id)

    if request.method == "POST":
        # Allow user to confirm a delete
        obj.delete()
        return redirect('home')

    context = {
        "object": obj
    }

    return render(request, "dim_sum/dimsum_lookup.html", context)
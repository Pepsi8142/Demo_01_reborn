from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
# from django.template import loader


# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'Food/index.html', context)


def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'Food/details.html', context)


def create_item(request):
    form = ItemForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect('Food:index')
    return render(request, 'Food/item-form.html', context)


def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    context = {
        'form': form,
        'item_id': item_id,
    }
    if form.is_valid():
        form.save()
        return redirect('Food:index')
    return render(request, 'Food/item-form.html', context)


def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    if request.method == 'POST':
        item.delete()
        return redirect('Food:index')
    return render(request, 'Food/item-delete.html', context)

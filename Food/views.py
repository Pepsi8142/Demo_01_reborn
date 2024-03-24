from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
# from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


# Class based views:
class IndexClassView(ListView):
    model = Item
    template_name = 'Food/index.html'
    context_object_name = 'item_list'


class DetailClassView(DetailView):
    model = Item
    template_name = 'Food/details.html'
    context_object_name = 'item'


class CreateItem(CreateView):
    model = Item
    fields = '__all__'
    template_name = 'Food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

# Function based views:
# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'Food/index.html', context)
#
#
# def details(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item
#     }
#     return render(request, 'Food/details.html', context)


# def create_item(request):
#     form = ItemForm(request.POST or None)
#     context = {
#         'form': form,
#     }
#     if form.is_valid():
#         form.save()
#         return redirect('Food:index')
#     return render(request, 'Food/item-form.html', context)


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

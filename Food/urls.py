from django.urls import path
from . import views

app_name = 'Food'
urlpatterns = [
    # /
    path('', views.index, name='index'),
    # /item/
    # path("item/", views.item, name='item'),
    # /item_id/
    path("<int:item_id>", views.details, name='details'),
    # add items
    path("add", views.create_item, name='create_item'),
    # edit items
    path("update/<int:item_id>", views.update_item, name='update_item'),
    # delete items
    path("delete/<int:item_id>", views.delete_item, name='delete_item'),

]

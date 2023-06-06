from LittleLemonApi.views import MenuItemsView
from django.urls import path, include 
urlpatterns = [
    path('menu-items/', MenuItemsView.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]

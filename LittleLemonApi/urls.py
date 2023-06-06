from LittleLemonApi.views import MenuItemsView, MenuItemsViewSet
from django.urls import path, include 
urlpatterns = [
    path('menu-items/', MenuItemsViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('menu-items/<int:pk>/', MenuItemsView.as_view()),
]

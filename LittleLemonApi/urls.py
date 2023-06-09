from django.urls import path, include 
from LittleLemonApi.views.menu_items_view_set import MenuItemsViewSet
from LittleLemonApi.views.menu_items_view import MenuItemsView
from LittleLemonApi.views.manager_view import ManagerView
from LittleLemonApi.views.delivery_crew_view import DeliveryCrewView
from LittleLemonApi.views.customer_view import CustomerView
from LittleLemonApi.views.order_view_set import OrderViewSet
from LittleLemonApi.views.order_view import OrderView

urlpatterns = [
    path('menu-items/', MenuItemsViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('menu-items/<int:pk>/', MenuItemsView.as_view()),
    path('groups/manager/users/',ManagerView.as_view() ),
    path('groups/delivery-crew/users/',DeliveryCrewView.as_view() ),
    path('cart/menu-items/', CustomerView.as_view()),
    path('orders/',OrderViewSet.as_view()),
    path('orders/<int:pk>',OrderView.as_view())
   
]
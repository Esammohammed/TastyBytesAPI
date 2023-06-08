
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from LittleLemonApi.models import Cart, Order, OrderItem
from LittleLemonApi.permissions import Permissions 
from rest_framework import status
from django.contrib.auth.models import User

from LittleLemonApi.serializers import OrderItemSerializer, OrderSerializer
class OrderView(APIView):

    serializer_class = OrderSerializer
    def post(self,request):
        if Permissions.is_customer(request):
            username= request.user
            user =User.objects.get(username=username)
            carts = Cart.objects.filter(user=user)
            total_price =0
            order =Order.objects.create(user=user, total=0, date= datetime.datetime.now())
            for cart in carts:
                total_price += cart.price
                OrderItem.objects.create(order=order, menuitem=cart.menuitem, quantity=cart.quantity,unit_price=cart.unit_price,price=cart.price)
            order.total = total_price
            order.save()
            carts.delete()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def get(self, request):
        if Permissions.is_customer(request):
            username = request.user
            orders = Order.objects.filter(user=username)
            serialized_orders = []
            
            for order in orders:
                order_items = OrderItem.objects.filter(order=order)
                serialized_order_items =OrderItemSerializer(order_items,many=True).data
                serialized_order = OrderSerializer(order).data
                serialized_order['items']= serialized_order_items
                serialized_orders.append(serialized_order)
            return Response(serialized_orders)
        return Response(status=status.HTTP_403_FORBIDDEN)
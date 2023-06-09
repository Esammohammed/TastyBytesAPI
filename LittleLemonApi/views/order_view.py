from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from LittleLemonApi.permissions import Permissions

from LittleLemonApi.models import Order, OrderItem
from LittleLemonApi.serializers import OrderItemSerializer, OrderSerializer
class OrderView (APIView):
    def get (self,request,pk):
        user = request.user
        order = get_object_or_404(Order,pk=pk,user=user)
        order_items = OrderItem.objects.filter(order=order)
        order_items = OrderItemSerializer(order_items,many=True).data
        serialized_order = OrderSerializer(order).data
        serialized_order['order_items'] = order_items
        return Response(serialized_order) 
    def patch(self,requset,pk):
        if Permissions.is_manager(requset) or Permissions.is_delivery_crew(requset):
            serialized_order= requset.data
            order = get_object_or_404 (Order,pk=pk)
            updated_order_serialized = OrderSerializer(order,serialized_order,partial=True)
            if (updated_order_serialized.is_valid()):
                updated_order_serialized.save()
                return Response(updated_order_serialized.data)
            
        return Response(updated_order_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

        
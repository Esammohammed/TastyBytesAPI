from rest_framework.views import APIView
from rest_framework.response import Response
from LittleLemonApi.models import Cart, MenuItem
from rest_framework import status
from LittleLemonApi.permissions import Permissions
from django.contrib.auth.models import User

class CustomerView (APIView):
    
    def get(self,request):
        if Permissions.is_customer(request):

            username= request.user
            items = Cart.objects.filter(user=username)
            return Response(items.values())
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def post(self,request):
        if Permissions.is_customer(request):
            username= request.user
            itemname= request.data['title']
            itemquantity= request.data['quantity']
            user =User.objects.get(username=username)
            menuitem = MenuItem.objects.get(title=itemname)
            unit_price = MenuItem.objects.get(title=itemname).price
            price = float(unit_price) * float (itemquantity)
            Cart.objects.create(user=user, menuitem=menuitem, quantity=itemquantity,unit_price=unit_price,price=price)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def delete(self,request):
        if Permissions.is_customer(request):
            username= request.user
            user =User.objects.get(username=username)
            carts = Cart.objects.filter(user=user)
            carts.delete()
            
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


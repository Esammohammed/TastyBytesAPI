from copy import deepcopy
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from LittleLemonApi.models import Cart, MenuItem, OrderItem
from rest_framework import status
from LittleLemonApi.serializers import MenuItemSerializer
from LittleLemonApi.permissions import Permissions
from django.contrib.auth.models import User, Group
from LittleLemonApi.serializers import MenuItemSerializer
# Create your views here.
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def create(self, request, *args, **kwargs):
        if Permissions.is_manager(request):
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def update(self, request, *args, **kwargs):
        if Permissions.is_manager(request):
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def destroy(self, request, *args, **kwargs):
        if Permissions.is_manager(request):
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

'''
MenuItemsView is a class-based view that inherits from generics.ListCreateAPIView. 
This view will be used to list, update, and delete single item.
'''
class MenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    '''
    The update and delete methods are overridden to check if the user is a manager.
    '''
    def update(self, request, *args, **kwargs):
        if Permissions.is_manager(request):
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, *args, **kwargs):
        if Permissions.is_manager(request):
            return super().delete(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
    


class ManagerView(APIView):
    '''
    This view will be used to list all the managers.
    '''
    def get(self, request, format=None):
        if Permissions.is_manager(request):
            all_managers = Group.objects.get(name='Manager')
            return Response(all_managers.user_set.values_list('username', flat=True))
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    '''
    This view will be used to add a new manager.
    '''
    def post(self, request, format=None):
        if Permissions.is_manager(request):
            new_manager = User.objects.get(username=request.data['username'])
            new_manager.groups.add(Group.objects.get(name='Manager'))
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)
    '''
    This delete method will be used to delete a manager.
    '''
    def delete (self, request, ):
        if Permissions.is_manager(request):
            deleted_manager = User.objects.get(username=request.data['username'])
            deleted_manager.groups.remove(Group.objects.get(name='Manager'))
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    
class DeliveryCrewView (APIView):
    def get(self, request, format=None):
        if Permissions.is_manager(request):
            all_delivery_crew = Group.objects.get(name='Delivery Crew')
            return Response(all_delivery_crew.user_set.values_list('username', flat=True))
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def post(self, request, format=None):
        if Permissions.is_manager(request):
            new_delivery_crew = User.objects.get(username=request.data['username'])
            new_delivery_crew.groups.add(Group.objects.get(name='Delivery Crew'))
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, format=None):
        if Permissions.is_manager(request):
            deleted_delivery_crew = User.objects.get(username=request.data['username'])
            deleted_delivery_crew.groups.remove(Group.objects.get(name='Delivery Crew'))
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    
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


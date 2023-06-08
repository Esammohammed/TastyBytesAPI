
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
    

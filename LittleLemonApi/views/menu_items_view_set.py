
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
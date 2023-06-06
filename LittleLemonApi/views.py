from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from LittleLemonApi.models import MenuItem
from rest_framework import status
from LittleLemonApi.serializers import MenuItemSerializer
from LittleLemonApi.permissions import Permissions

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
    
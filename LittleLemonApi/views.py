from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from LittleLemonApi.models import MenuItem
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
    
    
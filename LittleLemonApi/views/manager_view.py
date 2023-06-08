

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from LittleLemonApi.permissions import Permissions
from django.contrib.auth.models import User, Group
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
    
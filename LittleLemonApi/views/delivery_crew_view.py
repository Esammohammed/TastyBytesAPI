from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from LittleLemonApi.permissions import Permissions
from django.contrib.auth.models import User, Group
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
    
from django.shortcuts import render
from rest_framework import viewsets
from users.models import UserProfile
from contacts.serializers import usersSerializer


# Create your views here.
class usersViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = usersSerializer
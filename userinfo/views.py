from django.shortcuts import render
from rest_framework import generics

from .models import Userinfo
from .serializers import UserinfoSerializer


class UserinfoViewSet(generics.ListCreateAPIView):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer

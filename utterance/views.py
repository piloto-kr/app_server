from django.shortcuts import render
from rest_framework import generics

from .models import Utterance
from .serializers import UtteranceSerializer


class UtteranceViewSet(generics.ListCreateAPIView):
    queryset = Utterance.objects.all()
    serializer_class = UtteranceSerializer

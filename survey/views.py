from django.shortcuts import render
from rest_framework import generics

from .models import Survey
from .serializers import SurveySerializer


class SurveyViewSet(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

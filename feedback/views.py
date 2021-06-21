from django.shortcuts import render
from rest_framework import generics

from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewSet(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

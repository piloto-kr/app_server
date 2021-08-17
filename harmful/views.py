from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Harmful
from .serializers import HarmfulSerializer


class HarmfulViewSet(generics.ListCreateAPIView):
    queryset = Harmful.objects.all()
    serializer_class = HarmfulSerializer

    def get(self, request):
        uuid = request.GET.get("uuid", None)
        if uuid is None:
            queryset = Harmful.objects.all()
        else:
            date = request.GET.get("date", None)
            if date is None:
                queryset = Harmful.objects.filter(uuid=uuid)
            else:
                queryset = Harmful.objects.filter(uuid=uuid, date=date)

        serializer_class = HarmfulSerializer(queryset, many=True)
        return Response(serializer_class.data)

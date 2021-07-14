from django.shortcuts import render
from rest_framework import generics
from konlpy.tag import Kkma

from .models import Pit
from .serializers import PitSerializer
from .sentencestruct import SentenceStruct


class PitViewSet(generics.ListCreateAPIView):
    queryset = Pit.objects.all()
    serializer_class = PitSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()

        if self.request.data.get('pit_type') == 'sentence_struct':
            content = self.request.data.get('content')
            checklist = SentenceStruct().makeResultString(content)
            draft_request_data = self.request.data.copy()
            draft_request_data['checklist'] = checklist
            kwargs['data'] = draft_request_data
            return serializer_class(*args, **kwargs)
        return serializer_class(*args, **kwargs)

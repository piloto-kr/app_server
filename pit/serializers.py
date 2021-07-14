from rest_framework import serializers

from .models import Pit


class PitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pit
        fields = ['uuid', 'pit_type', 'checklist', 'content', 'checked_at']
        
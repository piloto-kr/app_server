from rest_framework import serializers

from .models import Harmful


class HarmfulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harmful
        fields = ['uuid', 'date', 'wordSet']

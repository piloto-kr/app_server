from rest_framework import serializers

from .models import PreferCharacter


class PreferCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferCharacter
        fields = ['uuid', 'prefer_character']

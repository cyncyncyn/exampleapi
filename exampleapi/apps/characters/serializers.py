from rest_framework import serializers

from .models import Character, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('url', 'name')

class CharacterSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Character
        fields = ('id', 'name', 'species', 'photos')

from django.shortcuts import render

# Create your views here.

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Character, Photo
from .serializers import CharacterSerializer, PhotoSerializer


class CharacterList(ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class PhotoList(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

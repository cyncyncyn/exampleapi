from django.shortcuts import render

# Create your views here.

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Character
from .serializers import CharacterSerializer


class CharacterList(ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

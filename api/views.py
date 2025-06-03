from django.shortcuts import render
from rest_framework import generics
from .models import Clipath
from .serializers import ClipathSerializer

class ClipathList(generics.ListAPIView):
    queryset = Clipath.objects.all()
    serializer_class = ClipathSerializer
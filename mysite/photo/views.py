from .models import Album, Photo
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .serializers import PhotoSerializer

from rest_framework import generics


class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo


class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

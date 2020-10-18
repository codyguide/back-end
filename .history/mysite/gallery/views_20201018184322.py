from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Gallery
from .serializers import GallerySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import F


class GalleryList(generics.ListCreateAPIView):
    queryset = Gallery.objects.all().order_by(
        '-created')
    serializer_class = GallerySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    parser_class = (FileUploadParser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def gallery(self, request, *args, **kwargs):

        fileserializer = GallerySerializer(data=request.data)

        if fileserializer.is_valid():
            fileserializer.save(user=self.request.user)
            return Response(fileserializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(fileserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GalleryDestroy(generics.RetrieveDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def get_queryset(self, **kwargs):
        queryset = Gallery.objects.filter(pk=self.kwargs['pk'])
        queryset.update(views=F('views') + 1)
        print("view 추가")
        return queryset

    def delete(self, request, *args, **kwargs):
        board = board.objects.filter(
            pk=self.kwargs['pk'], user=self.request.user)
        if board.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("ERROR")

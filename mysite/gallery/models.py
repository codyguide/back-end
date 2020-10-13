from django.db import models
from rest_framework import serializers

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer


# Create your models here.


class File(models.Model):
    file = models.ImageField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
# --업로드된 파일은 서버상에 해당 지정경로에 물리적으로 파일저장되고
# 저장된 파일의 정보만 models.FileField에 저장된다.


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

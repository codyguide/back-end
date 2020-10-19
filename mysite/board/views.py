from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Board, Comment
from .serializers import BoardSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import F


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all().order_by(
        '-created')
    serializer_class = BoardSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    parser_class = (FileUploadParser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def board(self, request, *args, **kwargs):

        fileserializer = BoardSerializer(data=request.data)

        if fileserializer.is_valid():
            fileserializer.save(user=self.request.user)
            return Response(fileserializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(fileserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDestroy(generics.RetrieveDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, **kwargs):
        queryset = Board.objects.filter(pk=self.kwargs['pk'])
        queryset.update(views=F('views') + 1)
        print("view 추가")
        return queryset

    def delete(self, request, *args, **kwargs):
        board = Board.objects.filter(
            pk=self.kwargs['pk'], user=self.request.user)
        if board.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError("ERROR")


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        board = Board.objects.get(pk=self.kwargs['pk'])
        return Comment.objects.filter(board=board).order_by(
            'created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Category(generics.ListAPIView):
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.filter(category=self.kwargs['category'])

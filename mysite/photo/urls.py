from django.urls import path
from photo import views

from django.views.generic import ListView, DetailView
from photo.models import Album, Photo


app_name = 'photo'
urlpatterns = [
    # /photo/
    path('', ListView.as_view(model=Album), name='index'),
    # /photo/album/ , same as /photo/
    path('', ListView.as_view(model=Album), name='album_list'),
    # /photo/album/99
    path('album/<int:pk>/', DetailView.as_view(model=Album), name='album_detail'),
    # /photo/album/99
    path('photo/<int:pk>/', DetailView.as_view(model=Photo), name='photo_detail'),

    path('photo/', views.PhotoList.as_view()),
]

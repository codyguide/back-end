"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

from django.contrib import admin
from django.urls import path, include, re_path

from member.views import regist_view, UserView, UserUpdateView

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views

schema_view = get_schema_view(
    openapi.Info(
        title="Weather Guide API 명세서",
        default_version='v1',
        description="날씨 코디 가이드 OPEN API 입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [


    path('admin/', admin.site.urls),
    # include()다른 URL 패턴을 포함 할 때는 항상 사용해야 합니다. admin.site.urls이것에 대한 유일한 예외입니다.
    path('api/get_token/', views.obtain_auth_token),
    path('api/register/', regist_view, name="register"),
    path("api/mypage/", UserView.as_view()),

    path('api/photo/', include('photo.urls')),

    path("api/mypage/<int:pk>/", UserUpdateView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/photo/', ListView.as_view(model=Album), name='index'),





    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)


# 어떤 URL을 정적으로 추가할래? > MEDIA_URL을 static 파일 경로로 추가
# 실제 파일은 어디에 있는데? > MEDIA_ROOT 경로내의 파일을 static 파일로 설정

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

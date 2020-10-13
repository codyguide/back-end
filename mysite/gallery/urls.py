
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # /api/booking/
    path('', views.BookingList.as_view()),

    # /api/booking/5
    path('<int:pk>/', views.BookingDetail.as_view()),

    # /api/booking/upload
    path('upload/', views.FileUploadView.as_view()),
]

urlpatterns = [

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

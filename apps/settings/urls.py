from django.urls import path
from apps.settings.views import *

urlpatterns = [
    path('gallery/', GalleryAPIView.as_view()),
    path('reviews/', ReviewAPIView.as_view()),
    path('otclicks/', OtklicAPIView.as_view()),
    path('otclicks/<int:pk>/', OtklicCreateAPIView.as_view()),
    path('', SettingsAPIView.as_view()),
]

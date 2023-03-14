from django.urls import path
from apps.countries.views import CountryAPIView, CountryUpdateAPIView, CountryCreateAPIView

urlpatterns = [
    path('', CountryAPIView.as_view()),
    path('<int:pk>/', CountryUpdateAPIView.as_view()),
    path('create/', CountryCreateAPIView.as_view()),
]

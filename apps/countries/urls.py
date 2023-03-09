from django.urls import path
from apps.countries.views import CountryAPIView, CountryUpdateAPIView

urlpatterns = [
    path('', CountryAPIView.as_view()),
    path('<int:pk>/', CountryUpdateAPIView.as_view()),
]

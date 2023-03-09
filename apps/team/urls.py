from django.urls import path
from apps.team.views import TechersAPIView

urlpatterns = [
    path('', TechersAPIView.as_view())
]

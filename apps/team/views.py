from rest_framework import generics
from apps.team.serializers import TeacherSerializer
from apps.team.models import Teacher

class TechersAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
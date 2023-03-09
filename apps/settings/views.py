from rest_framework import generics
from apps.settings.serializers import *
from apps.settings.models import Gallery, Review, Otklic

class GalleryAPIView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
class ReviewAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class OtklicAPIView(generics.ListAPIView):
    queryset = Otklic.objects.all()
    serializer_class = OtklicSerializer
class OtklicCreateAPIView(generics.CreateAPIView):
    queryset = Otklic.objects.all()
    serializer_class =OtklicSerializer
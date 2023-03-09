from rest_framework import serializers
from apps.settings.models import Review, Otklic, Gallery


class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = '__all__'
class OtklicSerializer(serializers.ModelSerializer):
    class Meta():
        model = Otklic
        fields = "__all__"
class GallerySerializer(serializers.ModelSerializer):
    class Meta():
        model = Gallery
        fields = "__all__"
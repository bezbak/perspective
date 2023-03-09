from rest_framework import generics
from apps.countries.models import Countries
from apps.countries.serializers import CountriesSerializer
# Create your views here.
class CountryAPIView(generics.ListAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    
class CountryUpdateAPIView(generics.UpdateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
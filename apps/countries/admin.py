from django.contrib import admin
from apps.countries.models import Countries

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
# Register your models here.

class CountryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Countries
        fields = '__all__'
        
@admin.register(Countries)       
class CountriesAdmin(admin.ModelAdmin):
    form = CountryAdminForm

# admin.site.register(Countries, CountriesAdmin)
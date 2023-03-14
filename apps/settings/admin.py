from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.settings.models import Otklic, Review, Gallery, Settings
# Register your models here.
@admin.register(Otklic)
class OtclicAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'call_phone', 'sity', 'message')
    list_display_links = ('full_name',)
    search_fields = ('sity',)
    
    def call_phone(self, obj):
        return mark_safe(f'<a href="tel:{obj.phone_number}">{obj.phone_number}</a>')
admin.site.register(Review)
admin.site.register(Gallery)
admin.site.register(Settings)
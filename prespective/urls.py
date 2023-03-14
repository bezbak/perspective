from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

api_urlpatterns = [
    path('team/', include('apps.team.urls')),
    path('settings/', include('apps.settings.urls')),
    path('countries/', include('apps.countries.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('api/', include(api_urlpatterns)),
    path('', TemplateView.as_view(template_name = 'index.html')),
    path('home/', TemplateView.as_view(template_name = 'index.html')),
    path('about/', TemplateView.as_view(template_name = 'index.html')),
    path('countries/', TemplateView.as_view(template_name = 'index.html')),
    path('countries/<str:slug>/', TemplateView.as_view(template_name = 'index.html')),
    path('contact/', TemplateView.as_view(template_name = 'index.html')),
    path('gallery/', TemplateView.as_view(template_name = 'index.html')),
    path('#/', TemplateView.as_view(template_name = 'index.html')),
    
]

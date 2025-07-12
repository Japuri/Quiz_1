from django.contrib import admin
from django.urls import path
from core.views import contact
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('projects/', include('projects.urls')),
path('contact/', contact, name='contact'),
]

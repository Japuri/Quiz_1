from django.urls import path
from .views import detail_view, project_detail
from django.urls import path, include


urlpatterns = [
    path('<int:id>/', detail_view, name='project_detail'),
path('', include('core.urls')),
path('projects/<int:id>/', project_detail, name='project_detail')

]

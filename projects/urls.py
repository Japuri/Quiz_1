from django.urls import path
from .views import detail_view

urlpatterns = [
    path('<int:id>/', detail_view, name='project_detail'),
]

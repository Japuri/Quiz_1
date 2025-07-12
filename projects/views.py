from django.shortcuts import render, get_object_or_404
from .models import Project

def detail_view(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'detail.html', {'project': project})

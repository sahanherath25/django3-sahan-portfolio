from django.shortcuts import render, get_object_or_404
from portfolio.models import Project


# Create your views here.
def home_page(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {"projects": projects})


def contents(request, content_id):
    content = get_object_or_404(Project, pk=content_id)
    return render(request, "portfolio/details.html", {"content": content})

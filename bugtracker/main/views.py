from django.shortcuts import render, redirect
from main.models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'main/project_list.html', {'projects': projects})

def create_project(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        Project.objects.create(title=title,description=description)
        return redirect('project_list')
    return render(request, 'main/project_form.html')

def project_detail():
    pass


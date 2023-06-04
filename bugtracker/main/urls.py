from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name="project_list"),
    path('projects/<int:pk>', views.project_detail, name="project_details"),
    path('projects/create', views.create_project, name="create_project"),
]
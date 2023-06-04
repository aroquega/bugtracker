from django.db import models

## test user, only for development right now
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects', null=True)
    collaborators = models.ManyToManyField(User)

class BugIssue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
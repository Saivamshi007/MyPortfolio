from django.db import models
from django.utils import timezone
class MessageTable(models.Model):
    message=models.TextField(max_length=20000)
    datetime=models.DateTimeField(default=timezone.now())

    def __str__(self) :
        return self.message +" "+str(self.datetime)
    
class ProjectTable(models.Model):
    project_title=models.TextField(max_length=100)
    project_abstract=models.TextField(max_length=800)
    project_tech=models.TextField(max_length=60)
    project_programming_background=models.TextField(max_length=60)
    project_link=models.TextField(max_length=100)

    def __str__(self) -> str:
        return "@".join([self.project_title,self.project_abstract,self.project_tech,
                self.project_programming_background,self.project_link])


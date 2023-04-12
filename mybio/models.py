from django.db import models
from django.utils import timezone
class MessageTable(models.Model):
    message=models.TextField(max_length=20000)
    datetime=models.DateTimeField(default=timezone.now())

    def __str__(self) :
        return self.message +" "+str(self.datetime)

# Create your models here.

from django.contrib import admin

from .models import MessageTable,ProjectTable

admin.site.register([MessageTable,ProjectTable])

# Register your models here.

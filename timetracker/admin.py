from django.contrib import admin
from .models import Employee, TimeEntry

admin.site.register(Employee)
admin.site.register(TimeEntry)
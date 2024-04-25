# timetracker/models.py

from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed, e.g., department, position, etc.

    def __str__(self):
        return self.user.username

class TimeEntry(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # Add other fields as needed, e.g., project, task, etc.

    def __str__(self):
        return f"{self.employee.user.username} - {self.start_time} to {self.end_time}"

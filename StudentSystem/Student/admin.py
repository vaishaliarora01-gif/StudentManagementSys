"""
This module defines the admin views for the Student app.

It includes models that are displayed in the admin site.
"""
from django.contrib import admin
from Student.models import Student,Domain

# Register your models here.

admin.site.register(Domain)
admin.site.register(Student)

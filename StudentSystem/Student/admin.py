from django.contrib import admin

# Register your models here.
from Student.models import Student,Domain

admin.site.register(Domain)

admin.site.register(Student)
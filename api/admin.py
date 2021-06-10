from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id','name','roll','city']

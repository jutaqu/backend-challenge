from django.contrib import admin
from .models import Task, Label


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "completion_status",
        "owner"
    ]


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner"
    ]

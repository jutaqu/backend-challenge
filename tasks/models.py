from django.db import models
from django.conf import settings


class Label(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="labels",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    labels = models.ManyToManyField(Label, blank=True)

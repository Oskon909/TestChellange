from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Property(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)


class Entity(models.Model):
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="modified_user"
    )
    value = models.IntegerField()
    properties = models.ManyToManyField("Property")

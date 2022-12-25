from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Property(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)


class Entity(models.Model):
    modified_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="modified_user"
    )
    value = models.IntegerField()
    properties = models.ManyToManyField("Property")

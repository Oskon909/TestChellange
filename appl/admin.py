from django.contrib import admin

# Register your models here.
from .models import Entity, Property, CustomUser

admin.site.register(CustomUser)
admin.site.register(Property)
admin.site.register(Entity)

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Platform, Link

admin.site.register(Platform)
admin.site.register(Link)
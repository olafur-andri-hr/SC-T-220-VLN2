from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User
u = User.objects.create_superuser("gudni", "email@example.com", "temp")

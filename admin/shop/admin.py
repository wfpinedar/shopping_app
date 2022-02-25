from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Order

# Register your models here.
admin.site.register(Order)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)
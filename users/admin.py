from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    list_display = ('username', 'email', 'is_active', 'is_staff', 'created_at')
    search_fields = ('email', 'username')
    ordering = ['-created_at']

admin.site.register(models.CustomUser, CustomUserAdmin)
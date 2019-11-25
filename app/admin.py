from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff',)


admin.site.register(User, MyUserAdmin)


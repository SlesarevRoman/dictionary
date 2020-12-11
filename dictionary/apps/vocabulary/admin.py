from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Word

class CustomWordAdmin(admin.ModelAdmin):
  list_display = ('author', 'word', 'definition', 'adding_date')

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'id')
    readonly_fields = ('id',)

admin.site.register(Word, CustomWordAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

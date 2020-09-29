from django.contrib import admin

from main.models import MainUser


@admin.register(MainUser)
class MainUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'address', 'decrypt')
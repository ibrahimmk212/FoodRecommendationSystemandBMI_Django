from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = []
    list_filter = []
    fieldsets = []


admin.site.register(Account,  AccountAdmin)

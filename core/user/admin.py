from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User


class UsersAdmin(ImportExportModelAdmin):
    list_display = ('username', 'email', 'date_joined')

    class Meta:
        model = User


admin.site.unregister(User)
admin.site.register(User, UsersAdmin)

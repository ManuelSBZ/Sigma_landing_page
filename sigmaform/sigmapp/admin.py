from django.contrib import admin
from .models import SingIn
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(SingIn)
class ViewAdmin(ImportExportModelAdmin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
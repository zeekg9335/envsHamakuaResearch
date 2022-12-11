from django.contrib import admin
from .models import Hamakua_Data
from .models import Hamakua_After_Disking  
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Hamakua_Data)
class data(ImportExportModelAdmin):
    pass

@admin.register(Hamakua_After_Disking)
class data(ImportExportModelAdmin):
    pass

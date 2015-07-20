from django.contrib import admin
from form.models import FarmDescription

class FarmDescriptionAdmin(admin.ModelAdmin):

    list_display = ('pk', 'farm_name', 'farm_description')

admin.site.register(FarmDescription,FarmDescriptionAdmin)
from django.contrib import admin
from .models import StudentsModel

# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display=['sno','sname','smark','saddr']

admin.site.register(StudentsModel,StudentsAdmin)
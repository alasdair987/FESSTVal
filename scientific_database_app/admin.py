from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.db import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from .models import Student, Professor, Device, Maintenance, Networks


class Student_Admin(admin.ModelAdmin):
    model = Student
    list_display = ('first_name', 'last_name', 'role')

admin.site.register(Student, Student_Admin)


class Professor_Admin(admin.ModelAdmin):
    model = Professor
    list_display = ('first_name', 'last_name', 'role')


admin.site.register(Professor, Professor_Admin)


class Device_Admin(ImportExportModelAdmin):
    date_hierarchy = 'register_date'
    model = Device
    list_display = ('device_name', 'device_type', 'register_date', 'device_user')

    pass


admin.site.register(Device, Device_Admin)


class Maintenance_Admin(ImportExportModelAdmin):
    model = Maintenance
    list_display = ('networks', 'description',
                    'timestamp', 'On-site maintenance?', 'Condition before maintenance', 'Condition after maintenance')

    pass


admin.site.register(Maintenance, Maintenance_Admin)

class Networks_Admin(ImportExportModelAdmin):
    model = Networks
    list_display = ('network_name', 'annotation1',
                    'annotation2', 'annotation3')

    pass


admin.site.register(Networks, Networks_Admin)
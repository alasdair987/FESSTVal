from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse


# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    u_number = models.IntegerField()

    def __str__(self):
        return self.first_name


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    u_number = models.IntegerField()


class Device(models.Model):
    # device_id = models.IntegerField()
    device_name = models.CharField(max_length=30)
    device_type = models.CharField(max_length=30)
    device_user = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    register_date = models.DateTimeField()

    def __str__(self):
        return self.device_name


class Maintenance(models.Model):
    devices = models.ForeignKey(Device, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    timestamp = models.DateTimeField()
    attribute1 = models.BooleanField()
    attribute2 = models.BooleanField()
    attribute3 = models.BooleanField()
    files = models.FileField(null=True, blank=True)

    def get_absolute_url(self):
        return "/maintenance-detail/%i" % self.id

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


class Networks(models.Model):
    network_name = models.CharField(max_length=30)
    annotation1 = models.CharField(max_length=30)
    annotation2 = models.CharField(max_length=30)
    annotation3 = models.CharField(max_length=30)

    def __str__(self):
        return self.network_name


class Device(models.Model):
    # device_id = models.IntegerField()
    device_name = models.CharField(max_length=30)
    device_type = models.CharField(max_length=30)
    device_user = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    register_date = models.DateTimeField()

    def __str__(self):
        return self.device_name


class Maintenance(models.Model):
    networks = models.ForeignKey(Networks, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    timestamp = models.DateTimeField()
    choice1 = models.CharField(name='On-site maintenance?', max_length=30, default='No', choices=[('yes', 'Yes'), ('no', 'No')])
    choice2 = models.CharField(name='Condition before maintenance', max_length=30, default='Active', choices=[('active', 'Active'), ('inactive', 'Inactive'),
                                                                         ('malfunction', 'Malfunction')])
    choice3 = models.CharField(name='Condition after maintenance', max_length=30, default='Active', choices=[('active', 'Active'), ('active_with_problems',
                                                                          'Active with Problems'), ('inactive',
                                                                                                    'Inactive')])
    files = models.FileField(null=True, blank=True)

    def get_absolute_url(self):
        return "/maintenance-detail/%i" % self.id




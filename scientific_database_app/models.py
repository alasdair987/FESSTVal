from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime
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

    def __unicode__(self):
        return self.network_name


class Device(models.Model):
    # device_id = models.IntegerField()
    associated_network = models.ForeignKey(Networks, on_delete=models.CASCADE, default=None)
    device_name = models.CharField(verbose_name="Name", default="Device Name", max_length=30)
    device_type = models.CharField(verbose_name="Type", default="Device Type", max_length=30)
    device_user = models.ForeignKey(Student, on_delete=models.CASCADE, default=None, verbose_name="User", )
    register_date = models.DateTimeField(verbose_name="Timestamp")

    def __str__(self):
        return self.device_name

    def __unicode__(self):
        return self.device_name


class Maintenance(models.Model):
    person_name = models.CharField(verbose_name='Name', max_length=30, default=None)
    networks = models.ForeignKey(Networks, on_delete=models.SET_NULL, null=True, default=None)
    associated_devices = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True, default=None)
    description = models.TextField(verbose_name='Description', default=None)
    timestamp = models.DateTimeField(verbose_name="Timestamp", default=datetime.now)
    choice1 = models.CharField(verbose_name='On-site?', max_length=30, default='No', choices=[('yes', 'Yes'), ('no', 'No')])
    choice2 = models.CharField(verbose_name='Condition before', max_length=30, default='Active', choices=[('active', 'Active'), ('inactive', 'Inactive'),
                                                                         ('malfunction', 'Malfunction')])
    choice3 = models.CharField(verbose_name='Condition after', max_length=30, default='Active', choices=[('active', 'Active'), ('active_with_problems',
                                                                          'Active with Problems'), ('inactive',
                                                                                                    'Inactive')])
    choice4 = models.CharField(verbose_name='Homogeneity', max_length=30, default='Not affected', choices=[('not affected', 'Not Affected'),
                                                                                                           ('maybe affected', 'Maybe Affected'),
                                                                                                           ('affected', 'Affected')])
    files = models.FileField(null=True, blank=True)

    def get_absolute_url(self):
        return "/maintenance-detail/%i" % self.id


class Measurement(models.Model):
    networks = models.ForeignKey(Networks, on_delete=models.CASCADE, default=None)
    measurement_name = models.CharField(verbose_name='Measurement Name', default=None, max_length=30)
    measurement_description = models.TextField(verbose_name='Measurement Description', default=None)
    location_description = models.TextField(default=None)
    position = models.CharField(max_length=30)
    files = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(verbose_name="Timestamp", default=datetime.now)


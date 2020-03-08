import django_tables2 as tables
from .models import Device, Maintenance, Measurement


class DeviceTable(tables.Table):
    class Meta:
        model = Device
        attrs = {'class': 'paleblue'}
        fields = ['device_name', 'device_type', 'device_user', 'register_date']


class MaintenanceTable(tables.Table):
    class Meta:
        model = Maintenance
        template_name = "django_tables2/bootstrap4.html"
        fields = ['id', 'networks', 'choice1', 'choice2', 'choice3', 'files', 'timestamp']
        attrs = {"class": "paleblue"}

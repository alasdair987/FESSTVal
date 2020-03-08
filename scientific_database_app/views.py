from django.shortcuts import render

# Create your views here.

from datetime import datetime
from pprint import pprint
from django_tables2 import RequestConfig
from .tables import DeviceTable, MaintenanceTable
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader

from bootstrap_datepicker_plus import DateTimePickerInput
from django.forms import Widget
from .forms import DeviceForm, MaintenanceForm, MeasurementForm
from .models import Student, Device, Maintenance


def home(request):
    students = Student.first_name
    # professors = Professor.first_name
    t = loader.get_template('/templates/site.html')
    c = Context({students})
    return HttpResponse(t.render(c))


def device_registration(request):
    devices = Device.objects.all()
    if request.method == "POST":
        form = DeviceForm(request.POST)

        if form.is_valid():
            pprint(request.POST)
            device = form.save(commit=False)
            device.save()
            return RegDevices(request)
        else:
            pprint("Invalid Form")
            return HttpResponse("Invalid form")
    else:
        form = DeviceForm()

    # c = Context({'object_list': devices})
    args = {'device_form': form, 'devices': devices}
    return render(request, 'device-registration.html', args)


def AddMaintenance(request):
    if request.method == 'POST':
        maintenance_form = MaintenanceForm(request.POST or None, request.FILES or None)
        if maintenance_form.is_valid():
            m1 = maintenance_form.save(commit=False)
            m1.save()
            messages.success(request, "Successfully created a Maintenance!")
            return HttpResponseRedirect('/maintenance-list/')
        else:
            HttpResponse("Invalid Form")

    else:
        maintenance_form = MaintenanceForm()
    return render(request, 'maintenance.html', {'maintenance_form': maintenance_form})


def AddMeasurement(request):
    if request.method == 'POST':
        measurement_form = MeasurementForm(request.POST or None, request.FILES or None)
        if measurement_form.is_valid():
            m2 = measurement_form.save(commit=False)
            m2.save()
            messages.success(request, "Successfully created a Maintenance!")
            return HttpResponseRedirect('/maintenance-list/')
        else:
            HttpResponse("Invalid Form")

    else:
        measurement_form = MeasurementForm()
    return render(request, 'measurement.html', {'measurement_form': measurement_form})


def RegDevices(request):
    table = DeviceTable(Device.objects.all())
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=5)

    #args = {'maintenance': maintenance}

    return render(request, 'device-list.html', {"table": table})


# class DeviceListView(SingleTableView):
#     model = Device
#     table_class = DeviceTable
#     template_name = 'device-list.html'


def MaintenanceList(request):
    table = MaintenanceTable(Maintenance.objects.all())
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=5)

    #args = {'maintenance': maintenance}

    return render(request, 'maintenance-list.html', {"table": table})


def MaintenanceDetail(request, id=None):
    obj = get_object_or_404(Maintenance, id=id)

    args = {'maintenance': obj}

    return render(request, "maintenance-detail.html", args)

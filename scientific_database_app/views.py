from django.shortcuts import render

# Create your views here.

from datetime import datetime
from pprint import pprint

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
            pprint(form.cleaned_data)
            device = form.save(commit=False)
            device.register_date = datetime.now()
            device.save()
            return RegDevices(request)
        else:
            pprint("Invalid Form")
            return HttpResponse("Invalid form")
    else:
        form = DeviceForm()

    # c = Context({'object_list': devices})
    args = {'Form': form, 'devices': devices}
    return render(request, 'device-registration.html', args)


def RegDevices(request):
    devices = Device.objects.all()
    # x = loader.get_template('/home/alasdair/Code/Python_Projects/templates/device-list.html')
    # c = Context({'object_list': devices})
    # return HttpResponse(x.render(c.flatten()))
    args = {'devices': devices}
    return render(request, 'device-list.html', args)


def AddMaintenance(request):
    if request.method == 'POST':
        maintenance_form = MaintenanceForm(request.POST or None, request.FILES or None)
        if maintenance_form.is_valid():
            m1 = maintenance_form.save(commit=False)
            m1.timestamp = datetime.today()
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
            m2.timestamp = datetime.today()
            m2.save()
            messages.success(request, "Successfully created a Maintenance!")
            return HttpResponseRedirect('/maintenance-list/')
        else:
            HttpResponse("Invalid Form")

    else:
        measurement_form = MeasurementForm()
    return render(request, 'measurement.html', {'measurement_form': measurement_form})


def MaintenanceList(request):
    maintenance = Maintenance.objects.all()

    args = {'maintenance': maintenance}

    return render(request, 'maintenance-list.html', args)


def MaintenanceDetail(request, id=None):
    obj = get_object_or_404(Maintenance, id=id)

    args = {'maintenance': obj}

    return render(request, "maintenance-detail.html", args)

from django.shortcuts import render

# Create your views here.

from datetime import datetime
from pprint import pprint

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader

from .forms import DeviceForm, MaintenanceForm
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
            pprint("Test1")
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
        pprint("Test3")
        form = DeviceForm()

    # c = Context({'object_list': devices})
    args = {'Form': form, 'devices': devices}
    pprint("Test4")
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
        pprint("Test")
        maintenance_form = MaintenanceForm(request.POST or None, request.FILES or None)
        pprint("Test2")
        if maintenance_form.is_valid():
            m1 = maintenance_form.save(commit=False)
            m1.timestamp = datetime.today()
            m1.save()
            pprint("Test4")
            messages.success(request, "Successfully created a Maintenance!")
            return HttpResponseRedirect('/maintenance-list/')
        else:
            HttpResponse("Invalid Form")

    else:
        pprint("Test5")
        maintenance_form = MaintenanceForm()
    pprint("Test3")
    return render(request, 'maintenance.html', {'maintenance_form': maintenance_form})


def MaintenanceList(request):
    maintenance = Maintenance.objects.all()

    args = {'maintenance': maintenance}

    return render(request, 'maintenance-list.html', args)


def MaintenanceDetail(request, id=None):
    obj = get_object_or_404(Maintenance, id=id)

    args = {'maintenance': obj}

    return render(request, "maintenance-detail.html", args)

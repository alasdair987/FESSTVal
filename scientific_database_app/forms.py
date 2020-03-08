from django import forms
import re, pprint, six
from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput, TimePickerInput

from django.forms import SelectDateWidget, MultiWidget, Select, Widget
from .models import Device, Maintenance, Measurement

# Choices for Maintenance Dropdowns
VOR_ORT_CHOICES= [
    ('ja', 'Ja'),
    ('nein', 'Nein'),
    ]


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'device_user',
            'device_name',
            'device_type']

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        pprint.pprint(self.fields['device_name'].widget.attrs)
        self.fields['device_name'].widget.attrs["class"] = "device_form_input"
        self.fields['device_type'].widget.attrs["class"] = "device_form_input"
        self.fields['device_user'].widget.attrs["class"] = "device_form_selection"

        # self.fields['device_name'].widget = forms.TextInput(attrs={
        #     'id': 'myCustomId',
        #     'class': 'myCustomClass',
        #     'name': 'myCustomName',
        #     'placeholder': 'myCustomPlaceholder'})


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = [
            'networks',
            'choice1',
            'choice2',
            'choice3',
            'description',
            'timestamp',
            'files']
        widgets = {
            'timestamp': DatePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        self.fields['networks'].widget.attrs["class"] = "device_form_input"
        self.fields['choice1'].widget.attrs["class"] = "device_form_choice1"
        self.fields['choice2'].widget.attrs["class"] = "device_form_choice2"
        self.fields['choice3'].widget.attrs["class"] = "device_form_choice3"
        self.fields['description'].widget.attrs["class"] = "device_form_input"
        self.fields['timestamp'].widget.attrs["class"] = "device_form_input"
        self.fields['files'].widget.attrs["class"] = "device_form_upload"
    #     _devices = forms.ModelMultipleChoiceField(queryset = None, required=False, widget=forms.SelectMultiple)

    # def __init__(self, *args, **kwargs):
    #     super(MaintenanceForm, self).__init__()
    #     devices = Device.objects.only('device_name')

    #     self.fields['_devices'].queryset = Device.objects.filter(device_name=devices)


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'networks',
            'measurement_name',
            'measurement_description',
            'location_description',
            'position',
            'files'
        ]

    def __init__(self, *args, **kwargs):
        super(MeasurementForm, self).__init__(*args, **kwargs)
        self.fields['networks'].widget.attrs["class"] = "measurement_form_input"
        self.fields['measurement_name'].widget.attrs["class"] = "measurement_form_name"
        self.fields['measurement_description'].widget.attrs["class"] = "measurement_form_description"
        self.fields['location_description'].widget.attrs["class"] = "location_form_description"
        self.fields['position'].widget.attrs["class"] = "position_form_input"
        self.fields['files'].widget.attrs["class"] = "measurement_form_upload"

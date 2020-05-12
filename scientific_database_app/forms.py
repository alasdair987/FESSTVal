from django import forms
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
            'device_type',
            'register_date',
        ]
        widgets = {
            'register_date': DateTimePickerInput()
        }

    # def __init__(self, *args, **kwargs):
    #     super(DeviceForm, self).__init__(*args, **kwargs)
    #     pprint.pprint(self.fields['device_name'].widget.attrs)
    #     self.fields['device_name'].widget.attrs["class"] = "device_form_input"
    #     self.fields['device_type'].widget.attrs["class"] = "device_form_input"
    #     self.fields['device_user'].widget.attrs["class"] = "device_form_selection"

        # self.fields['device_name'].widget = forms.TextInput(attrs={
        #     'id': 'myCustomId',
        #     'class': 'myCustomClass',
        #     'name': 'myCustomName',
        #     'placeholder': 'myCustomPlaceholder'})


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = [
            'person_name',
            'networks',
            'associated_devices',
            'choice1',
            'choice2',
            'choice3',
            'choice4',
            'description',
            'timestamp',
            'files']
        widgets = {
            'timestamp': DateTimePickerInput(),
            'person_name': forms.TextInput(attrs={'placeholder': 'Type your name here'}),
            'description': forms.Textarea(attrs={'placeholder': 'Type your description here'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['associated_devices'].queryset = Device.objects.none()

        if 'networks' in self.data:
            try:
                associated_network_id = int(self.data.get('networks'))
                self.fields['associated_devices'].queryset = Device.objects.filter(associated_network_id=associated_network_id).order_by('associated_network__network_name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['associated_devices'].queryset = self.instance.networks.associated_devices_set.order_by('associated_network__network_name')


    # def __init__(self, *args, **kwargs):
    #     super(MaintenanceForm, self).__init__(*args, **kwargs)
    #     self.fields['networks'].widget.attrs["class"] = "device_form_input"
    #     self.fields['choice1'].widget.attrs["class"] = "device_form_choice1"
    #     self.fields['choice2'].widget.attrs["class"] = "device_form_choice2"
    #     self.fields['choice3'].widget.attrs["class"] = "device_form_choice3"
    #     self.fields['description'].widget.attrs["class"] = "device_form_input"
    #     self.fields['timestamp'].widget.attrs["class"] = "device_form_input"
    #     self.fields['files'].widget.attrs["class"] = "device_form_upload"
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
            'timestamp',
            'files',
        ]
        widgets = {
            'timestamp': DateTimePickerInput(),
            'measurement_name': forms.TextInput(attrs={'placeholder': ''}),
            'measurement_description': forms.Textarea(attrs={'placeholder': 'Type your description here'}),
            'location_description': forms.Textarea(attrs={'placeholder': 'Type your description here'})
        }

    # def __init__(self, *args, **kwargs):
    #     super(MeasurementForm, self).__init__(*args, **kwargs)
    #     self.fields['networks'].widget.attrs["class"] = "measurement_form_input"
    #     self.fields['measurement_name'].widget.attrs["class"] = "measurement_form_name"
    #     self.fields['measurement_description'].widget.attrs["class"] = "measurement_form_description"
    #     self.fields['location_description'].widget.attrs["class"] = "location_form_description"
    #     self.fields['position'].widget.attrs["class"] = "position_form_input"
    #     self.fields['files'].widget.attrs["class"] = "measurement_form_upload"

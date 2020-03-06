from pprint import pprint
from django import  forms

from django.forms import ModelForm

from .models import Device, Maintenance

# Choices for Maintenance Dropdowns

VOR_ORT_CHOICES= [
    ('ja', 'Ja'),
    ('nein', 'Nein'),
    ]


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = [
            'device_user',
            'device_name',
            'device_type']

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        pprint(self.fields['device_name'].widget.attrs)
        self.fields['device_name'].widget.attrs["class"] = "device_form_input"
        self.fields['device_type'].widget.attrs["class"] = "device_form_input"
        self.fields['device_user'].widget.attrs["class"] = "device_form_selection"

        # self.fields['device_name'].widget = forms.TextInput(attrs={
        #     'id': 'myCustomId',
        #     'class': 'myCustomClass',
        #     'name': 'myCustomName',
        #     'placeholder': 'myCustomPlaceholder'})


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = [
            'networks',
            'On-site maintenance?',
            'Condition before maintenance',
            'Condition after maintenance',
            'description',
            'files',
        ]


    def __init__(self, *args, **kwargs):
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        self.fields['networks'].widget.attrs["class"] = "device_form_input"
        self.fields['On-site maintenance?'].widget.attrs["class"] = "device_form_choice1"
        self.fields['Condition before maintenance'].widget.attrs["class"] = "device_form_choice2"
        self.fields['Condition after maintenance'].widget.attrs["class"] = "device_form_choice3"
        self.fields['description'].widget.attrs["class"] = "device_form_input"
        self.fields['files'].widget.attrs["class"] = "device_form_upload"
    #     _devices = forms.ModelMultipleChoiceField(queryset = None, required=False, widget=forms.SelectMultiple)

    # def __init__(self, *args, **kwargs):
    #     super(MaintenanceForm, self).__init__()
    #     devices = Device.objects.only('device_name')

    #     self.fields['_devices'].queryset = Device.objects.filter(device_name=devices)

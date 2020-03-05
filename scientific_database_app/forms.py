from pprint import pprint

from django.forms import ModelForm

from .models import Device, Maintenance


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
            'devices',
            'attribute1',
            'attribute2',
            'attribute3',
            'description',
            'files']

    def __init__(self, *args, **kwargs):
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        self.fields['devices'].widget.attrs["class"] = "device_form_input"
        self.fields['attribute1'].widget.attrs["class"] = "device_form_attribute"
        self.fields['attribute2'].widget.attrs["class"] = "device_form_attribute"
        self.fields['attribute3'].widget.attrs["class"] = "device_form_attribute"
        self.fields['description'].widget.attrs["class"] = "device_form_input"
        self.fields['files'].widget.attrs["class"] = "device_form_upload"
    #     _devices = forms.ModelMultipleChoiceField(queryset = None, required=False, widget=forms.SelectMultiple)


    # def __init__(self, *args, **kwargs):
    #     super(MaintenanceForm, self).__init__()
    #     devices = Device.objects.only('device_name')

    #     self.fields['_devices'].queryset = Device.objects.filter(device_name=devices)

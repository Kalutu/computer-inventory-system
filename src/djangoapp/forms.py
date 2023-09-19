from django import forms
from .models import Computer, Operating_system

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'IP_address', 'MAC_address', 'operating_system', 'users_name', 'location', 'purchase_date']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'class': 'dateinput'}),
        }
    def clean_computer_name(self):
        computer_name = self.cleaned_data.get('computer_name')
        if (computer_name == ""):
            raise forms.ValidationError('This field cannot be left blank')
        instance = self.instance
        existing_computers = Computer.objects.exclude(id=instance.id)
        for computer in existing_computers:
            if computer.computer_name == computer_name:
                raise forms.ValidationError(computer_name + ' is already added')
        
        return computer_name

    def clean_users_name(self):
        users_name = self.cleaned_data.get('users_name')
        if (users_name == ""):
            raise forms.ValidationError('This field cannot be left blank')

        instance = self.instance
        existing_computers = Computer.objects.exclude(id=instance.id)
        for computer in existing_computers:
            if computer.users_name == users_name:
                raise forms.ValidationError(users_name + ' is already added')
        
        return users_name


class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'users_name', 'export_to_CSV']

class OperatingSystemForm(forms.ModelForm):
  class Meta:
   model =  Operating_system
   fields = ['operating_system']

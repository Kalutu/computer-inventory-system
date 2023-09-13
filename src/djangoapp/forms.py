from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
   class Meta:
     model = Computer
     fields = ['computer_name', 'IP_address', 'MAC_address', 'users_name', 'location']
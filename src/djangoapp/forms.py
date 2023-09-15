from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'IP_address', 'MAC_address', 'users_name', 'location', 'purchase_date']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'class': 'dateinput'}),
        }
class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'users_name']
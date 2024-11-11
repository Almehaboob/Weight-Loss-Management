# forms.py
from django import forms
from .models import WeightEntry

class AddWeightForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ['weight'] 
        


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
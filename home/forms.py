import form as form
from django import forms
from .models import home_profiles
#from bootstrap_datepicker_plus.widgets import DatePickerInput

class homeform(forms.ModelForm):
    #pickup_date = forms.DateField(widget=DatePickerInput())
    class Meta:
        model = home_profiles
        fields = "__all__"
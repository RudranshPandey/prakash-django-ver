import form as form
from django import forms
from .models import All_profiles
from bootstrap_datepicker_plus.widgets import DatePickerInput

class AllProfileForm(forms.ModelForm):
    pickup_date = forms.DateField(widget=DatePickerInput())
    class Meta:
        model = All_profiles
        fields = "__all__"
        #forms.fields['pickup_date'] = DateTimePickerInput(attrs={'type':'datetime-local'})
        # exclude = ('pickup_date','gender')
        # fields = ('memo_no','first_name')




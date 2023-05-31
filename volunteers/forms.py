import form as form
from django import forms
from .models import volunteer_profiles
#from bootstrap_datepicker_plus.widgets import DatePickerInput

class volunteerform(forms.ModelForm):
    #pickup_date = forms.DateField(widget=DatePickerInput())
    class Meta:
        model = volunteer_profiles
        fields = "__all__"
        #forms.fields['pickup_date'] = DateTimePickerInput(attrs={'type':'datetime-local'})
        # exclude = ('pickup_date','gender')
        # fields = ('memo_no','first_name')




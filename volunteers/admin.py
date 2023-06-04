from django.contrib import admin
from .models import volunteer_profiles

#admin.site.register(volunteer_profiles)
class volunteer_profile(admin.ModelAdmin):
    list_display = ['volunteer_no','first_name','last_name','phone_number']
# Register your models here.
admin.site.register(volunteer_profiles,volunteer_profile)

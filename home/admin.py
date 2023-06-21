from django.contrib import admin
from .models import home_profiles

#admin.site.register(volunteer_profiles)
class home_profile(admin.ModelAdmin):
    list_display = ['home_name','home_address','phone_number','contact_person','category','beds']
# Register your models here.
admin.site.register(home_profiles,home_profile)

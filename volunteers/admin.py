from django.contrib import admin
from .models import volunteer_profiles

admin.site.register(volunteer_profiles)
class All_Profile(admin.ModelAdmin):
    list_display = ['volunteer_no','first_name','last_name']
# Register your models here.

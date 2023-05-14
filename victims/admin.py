from django.contrib import admin
from django.contrib import admin
from .models import All_profiles

admin.site.site_header = "Kaval Karengal Dashboard"
admin.site.index_title = "Prakash"
class All_profile(admin.ModelAdmin):
    list_display = ['memo_no','pickup_location'] #Empadmin is a superclass present in django.contrib in admin folder that allows for editing display
    readonly_fields = ('imgpreview',)
    #list_filter = ['zone']
admin.site.register(All_profiles,All_profile)  #second parameter is legit the customization of table that will show in the admin page

from django.urls import path
from . import views
from .views import addvictim,index,update_view




app_name = "victims"
urlpatterns = [
    path("add",addvictim,name="add"),
    path("index",index,name="index"),
    path("update/<str:pk>/",update_view,name="update_view"),
    path("victims/",views.victims_list),
    path("victims/<str:id>",views.victims_detail),
    path("victimsglobalview/",views.globally_view_victims,name="victimsglobalview"),
]
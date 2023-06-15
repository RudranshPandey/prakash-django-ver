from django.urls import path
from . import views
from .views import addvictim,index,update_view




app_name = "victims"
urlpatterns = [
    path("add",addvictim,name="add"),
    path("index",index,name="index"),
    path("update/<int:pk>/",update_view,name="update_view"),
    path("victims/",views.victims_list),
]
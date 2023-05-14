from django.urls import path
from .views import addvictim,index

app_name = "victims"
urlpatterns = [
    path("add",addvictim,name="add"),
    path("index",index,name="index")
]
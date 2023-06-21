from django.urls import path

from . import views
from .views import index,addhome,update_view

app_name = "home"
urlpatterns = [
    path("add", addhome, name="add"),
    path("index", index, name="index"),
    path("update/<str:pk>/", update_view, name="update_view")
]
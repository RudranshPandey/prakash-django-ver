from django.shortcuts import render,redirect,reverse
from .forms import AllProfileForm
from .models import All_profiles

def addvictim(request):

    form = AllProfileForm()
    if request.method == "POST":
        form = AllProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("victims:index"))
    return render(request,"victims/add.html",{"form":form})

def index(request):
    victims = All_profiles.objects.all()
    return render(request,"victims/index.html",{"victims":victims})
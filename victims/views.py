from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    victims = All_profiles.objects.all().order_by('-pickup_date')
    return render(request,"victims/index.html",{"victims":victims})

def update_view(request, pk):
    object = get_object_or_404(All_profiles,pk=pk)  # Use the passed pk argument instead of hardcoding it
    if request.method == "POST":
        form = AllProfileForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect(reverse("victims:index"))
    else:
        form = AllProfileForm(instance=object)
    return render(request,"victims/update.html", {"form": form, "object": object})

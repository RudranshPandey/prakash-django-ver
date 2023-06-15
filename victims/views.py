from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import AllProfileForm
from .models import All_profiles
from django.http import JsonResponse
from .serializers import All_profilesSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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


@api_view(['GET','POST'])
def victims_list(request):
    if request.method == 'GET':
        victims = All_profiles.objects.all()
        serializer = All_profilesSerializers(victims,many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        serializer = All_profilesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





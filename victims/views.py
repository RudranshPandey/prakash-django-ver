from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import AllProfileForm
from .models import All_profiles
from django.http import JsonResponse
from .serializers import All_profilesSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

def addvictim(request):

    form = AllProfileForm()
    if request.method == "POST":
        form = AllProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("victims:index"))
    return render(request,"victims/add.html",{"form":form})

def index(request):
    victims = All_profiles.objects.all().order_by('-id') 
    p = Paginator(All_profiles.objects.all(),1)
    page = request.GET.get('page')
    victims_per_page = p.get_page(page)
    nums = "a" * victims_per_page.paginator.num_pages
    return render(request,"victims/index.html",{"victims":victims,'victims_per_page':victims_per_page,'nums': nums})

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

@api_view(['GET','PUT','DELETE'])
def victims_detail(request, id):

    try:
       victims = All_profiles.objects.get(pk=id)
    except All_profiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = All_profilesSerializers(victims)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = All_profilesSerializers(victims, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        victims.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







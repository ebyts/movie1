from django.shortcuts import render, HttpResponse , redirect
from . models import Movie 
from . form import Movieform

from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.






def first(request):
    return render(request,'first.html')



def index(request):
    movie=Movie.objects.all()
    context={
            'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie':movie})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dir=request.POST.get('director')
        year=request.POST.get('year')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        movie=Movie(name=name,director=dir,year=year,desc=desc,img=img)
        movie.save();
    return render(request,'add.html')


def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

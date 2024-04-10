from django.shortcuts import render
from first_app import models
from first_app import forms

# Create your views here.


def index(request):
    musician_list = models.Musician.objects.order_by('first_name')
    diction = {'title':'Home','musician_list':musician_list}
    return render(request, 'first_app/index.html', context=diction)

def album_list(request, musician_id):
    musician_details = models.Musician.objects.get(pk=musician_id)
    album_list = models.Album.objects.filter(artist=musician_id)
    diction = {'title':'Album List','musician':musician_details,'album_list':album_list}
    return render(request, 'first_app/album_list.html', context=diction)

def add_musician(request):
    musician_form = forms.MusicianForm()

    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)

        if musician_form.is_valid():
            musician_form.save(commit=True)
            return index(request)
        
    diction = {'title':'Add Musician', 'musician_form':musician_form }
    return render(request, 'first_app/musician_form.html', context=diction)

def add_album(request):
    album_form = forms.AlbumForm()

    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)

        if album_form.is_valid():
            album_form.save(commit=True)
            return index(request)

    diction = {'title':'Album List','album_form':album_form}
    return render(request, 'first_app/album_form.html', context=diction)


def edit_musician(request,musician_id):
    musician = models.Musician.objects.get(pk=musician_id)
    musician_form = forms.MusicianForm(instance=musician)

    if request.method == "POST":
        musician_form = forms.MusicianForm(request.POST, instance=musician)

        if musician_form.is_valid():
            musician_form.save(commit=True)
            return index(request)


    diction = {'title':'Edit Musician', 'musician_form':musician_form}
    return render(request, 'first_app/edit_musician.html',context=diction)


def edit_alum(request,album_id):
    album_list = models.Album.objects.get(pk=album_id)
    album_form = forms.AlbumForm(instance=album_list)
    diction = {}

    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album_list)

        if album_form.is_valid():
            album_form.save(commit=True)
            diction.update({'updated':'Successfully updated'})


    diction.update({"album_form":album_form})
    diction.update({'album_id':album_id})
    return render(request, 'first_app/edit_album.html',context=diction)

def delete_album(request,album_id):
    album_delete = models.Album.objects.get(pk=album_id).delete()
    diction = {'Deleted':'Deleted Successfully'}
    return render(request, 'first_app/delete.html', context=diction)

def delete_musician(request,musician_id):
    musician_delete = models.Musician.objects.get(pk=musician_id).delete()
    diction = {'Deleted':'Deleted Successfully'}
    return render(request, 'first_app/delete.html', context=diction)
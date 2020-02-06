from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views.generic import ListView, CreateView
from mainapp.models import Song, UserPlaylists, User, Playlists
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from mainapp.forms import AddSong

###################################################### Logout View ##################################################################

def LogoutView(request):
    '''this view  to logout the loged in user '''
    auth.logout(request)
    return redirect(reverse_lazy("songs"))
###################################################### Login View ##################################################################



def LoginView(request):
    '''this view  to open the login  page '''
    if request.method == "POST":
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('songs')
        else:
            messages.info(request, 'UserName or password are not correct')
            return redirect('login')
    else:
        return render(request, "login.html")


###################################################### Songs View ##################################################################
def SongView(request):

    ''' this view present all songs for the user and he can add a song to a playlisy buy choosing the play list from a drop down menu '''
    CTX = {}

    # bring all songs from data base and post them in the page 
    songs_list = Song.objects.all()
    CTX['songs_list'] = songs_list

    # bring all playlists from userplaylists to show them in the drop down list 
    Playlist = UserPlaylists.objects.filter(user_id=request.user.id)
    CTX['Playlists'] = Playlist

    #if user want added a song to a play list 

    if(request.method == "POST"):
        if request.user.id == None:
            return redirect('login')
        else:
            #pring song id and userplaylist id
            data = request.POST['hhh']
            split_data = data.split("+")
            #user play list id 
            playlist_id = split_data[0]
            print(playlist_id)
            #song id 
            song_id = split_data[1]
            print(song_id)

            #create new playlist object  ( table between the userplay list table and songs)
            playlist = Playlists()
            up = UserPlaylists.objects.get(id=playlist_id)
            s = Song.objects.get(id=song_id)
            playlist.UserPlaylist = up
            playlist.song = s
            playlist.save()

    return render(request, "songs.html", CTX)

###################################################### Play List(s) View ##################################################################

def PlayListsView(request):
    ''' bring playlists  from data base and present them on the  playlists.html page for the loged in user   '''
    CTX = {}
    playlist = UserPlaylists.objects.filter(user_id=request.user.id)
    CTX['Playlists'] = playlist
    return render(request, "playlists.html", CTX)

###################################################### Play List View ##################################################################
def PlayListView(request, pn):
    ''' this page  the chosen playlist and also all songs and you can add song to play list from this page  and upload a song also  '''
    #context
    CTX = {}
    #bring playlists from database
    playlists = Playlists.objects.filter(UserPlaylist_id=pn)
    # list to add the uniqe songs to it
    c = []
    # list to check if the song is the previeus list or not to prevent redunduncy
    b = []
    # to remove duplicated songs  in  playlist the view 
    for i in playlists:
        if i.song not in b:
            b.append(i.song)
            c.append(i)
    CTX['playlists'] = c
    #to show all songs in the view 
    CTX['songs'] = Song.objects.all()
    #from  to enable users to add songs to the website
    form = AddSong()
    CTX['form'] = form

    #if the user want to add a song to the open playlist 
    if request.method == 'POST':
        if request.user.id == None:
            return redirect('login')
        else:
            print(request.POST['id'])
            song_id = request.POST['id']
            print(song_id)
            #specifiy User playlist id 
            up = UserPlaylists.objects.get(id=pn)
            #specify Song id 
            s2 = Song.objects.get(id=song_id)
            #create object and save it 
            playlist = Playlists()
            playlist.UserPlaylist = up
            playlist.song = s2
            playlist.save()

    return render(request, "playlist.html", CTX)

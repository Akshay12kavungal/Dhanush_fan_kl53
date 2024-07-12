from django.utils import timezone 
from django.shortcuts import redirect, render

from .models import Award, Biography, Filmography, Movie,Photo, Video, Comment

# Create your views here.


def home(request):
 
    biography = Biography.objects.first()

    filmography = Filmography.objects.all().order_by('-year')[:5]
    
    awards = Award.objects.all()[:5]

    latest_movies =  Movie.objects.filter(status='released').order_by('-release_date')[:4]

    upcoming_movies =  Movie.objects.filter(status='upcoming').order_by('-release_date')[:4]
    
    context = {
        'biography': biography,
        'filmography': filmography,
        'awards': awards,
        'latest_movies': latest_movies,
        'upcoming_movies':upcoming_movies
       
    }
    return render(request, 'fanpage/home.html', context)


def biography(request):
    biography = Biography.objects.first()
    return render(request, 'fanpage/biography.html', {'biography': biography})

def upcoming_movies(request):
    upcoming_movies =  Movie.objects.filter(status='upcoming').order_by('-release_date')
    return render(request, 'fanpage/upcoming_movies.html', {'upcoming_movies': upcoming_movies})

def movie_list(request):
    movie_lists = Movie.objects.all().order_by('-release_date',)
    context = {
        'movie_lists': movie_lists
    }
    return render(request, 'fanpage/movie_list.html', context)

def latest_movie(request):
    latest=Movie.objects.filter(status='released').order_by('-release_date')
    context={
        'latest':latest
    }
    return render(request,'fanpage/latest_movies.html',context)
    

def movie_detail(request,pk):
    movie=Movie.objects.get(pk=pk)
    return render(request,'fanpage/movie_detail.html',{'movie':movie})


def awards(request):
    awards=Award.objects.all()
    return render(request,'fanpage/awards.html',{'awards':awards})




def photo_gallery(request):
    photos=Photo.objects.all()
    movie_list=Movie.objects.all()
    context={
        'photos':photos,
        'movie_list':movie_list
    }
    return render(request,'fanpage/photo_gallery.html',context)


def video_gallery(request):
    videos=Video.objects.all()
    return render(request,'fanpage/video_gallery.html',{'videos':videos})


def comments(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        if author and text:
            comment = Comment(author=author, text=text, created_date=timezone.now())  # Use timezone.now()
            comment.save()
            return redirect('comments')
    comments = Comment.objects.order_by('-created_date')[:5]
    return render(request, 'fanpage/comments.html', {'comments': comments})

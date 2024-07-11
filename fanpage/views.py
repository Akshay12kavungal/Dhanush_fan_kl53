from django.utils import timezone 
from django.shortcuts import redirect, render

from .models import Movie, NewsArticle,Photo, Video, Comment

# Create your views here.


def home(request):
    latest_movies=Movie.objects.order_by('-release_date')[:5]
    recent_news=NewsArticle.objects.order_by('-publication_date')[:5]

    context={'latest_movies':latest_movies,
             'recent_news':recent_news,
             }

    return render(request,'fanpage/home.html',context)

def movie_detail(request,pk):
    movie=Movie.objects.get(pk=pk)
    return render(request,'fanpage/movie_detail.html',{'movie':movie})


def news_list(request):
    news_articles=NewsArticle.objects.order_by('-publication_date')
    return render(request,'fanpage/news_list.html',{'news_articles': news_articles})


def photo_gallery(request):
    photos=Photo.objects.all()
    return render(request,'fanpage/photo_gallery.html',{'photos':photos})


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
    comments = Comment.objects.order_by('-created_date')
    return render(request, 'fanpage/comments.html', {'comments': comments})

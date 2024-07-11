from django.urls import path
from . import views

urlpatterns =[

    path('',views.home, name='home'),
    path('movies/<int:pk>/',views.movie_detail,name='movie_detail'),
    path('news/', views.news_list, name='news_list'),
    path('photos/', views.photo_gallery, name='photo_gallery'),
    path('videos/', views.video_gallery, name='video_gallery'),
    path('comments/', views.comments, name='comments'),


]
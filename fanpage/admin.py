from django.contrib import admin

from .models import Award, Biography, Filmography, Movie, MovieList, NewsArticle, Photo,Comment, RelatedLinks, Video

# Register your models here.

@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display=('title','release_date','poster','description','trailer_link')
    search_fields=('title','release_date')
    list_filter=('title','release_date')

@admin.register(MovieList)
class MovieListAdmin(admin.ModelAdmin):
    list_display=('title','year','image','description')
    search_fields=('title','year')
    list_filter=('title','year')



@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display=('title','publication_date','summary','read_more_link')
    search_fields=('title','publication_date')
    list_filter=('title','publication_date')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=('title','image','description')
    search_fields=('title',)
    list_filter=('title',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display=('title','video_link','description')
    search_fields=('title',)
    list_filter=('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('author','text','created_date')
    search_fields=('author','created_date')
    list_filter=('author','created_date')



@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Filmography)
class FilmographyAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'role')
    list_filter = ('year',)
    search_fields = ('title', 'role')

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(RelatedLinks)
class RelatedLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title',)
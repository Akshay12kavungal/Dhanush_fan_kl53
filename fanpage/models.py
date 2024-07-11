from django.db import models

# Create your models here.


class Movie(models.Model):
    title=models.CharField(max_length=200)
    release_date=models.DateField()
    poster=models.ImageField(upload_to='posters/')
    description=models.TextField()
    trailer_link=models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class MovieList(models.Model):
    title = models.CharField(max_length=200)
    year=models.DateField()
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='movie_lists/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class NewsArticle(models.Model):
    title=models.CharField(max_length=200)
    publication_date=models.DateField()
    summary=models.TextField()
    read_more_link=models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Photo(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='photos/')
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title=models.CharField(max_length=200)
    video_link=models.URLField()
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author=models.CharField(max_length=100)
    text=models.TextField()
    created_date=models.DateTimeField(auto_created=True)



    def __str__(self):
        return f"{self.author} - {self.created_date}"


class Biography(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Filmography(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()

class Award(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class RelatedLinks(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

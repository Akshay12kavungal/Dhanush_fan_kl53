from django.db import models

# Create your models here.

class Movie(models.Model):
    STATUS_CHOICES = [
        ('released', 'Released Movie'),
        ('upcoming', 'Upcoming Movie'),
    ]

    title = models.CharField(max_length=200)
    release_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    trailer_link = models.URLField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='released')

    def __str__(self):
        return self.title
    
    @property
    def status_display(self):
        return self.get_status_display().capitalize()


    
class Photo(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='photos/')
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title=models.CharField(max_length=200)
    video_link=models.URLField()
    video_file = models.FileField(upload_to='videos/', blank=True)
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
    title = models.CharField(max_length=200, default='Biography of Dhanush')
    about = models.TextField(default='About Dhanush content here.')
    early_life = models.TextField(default='Early life content here.')
    personal_life = models.TextField(default='Personal life content here.')
    movie_career_actor = models.TextField(default='Movie career as an actor content here.')
    movie_career_producer = models.TextField(default='Movie career as a producer content here.')
    movie_career_director = models.TextField(default='Movie career as a director content here.')
    image = models.ImageField(upload_to='Biography/', default='default_biography_image.jpg')

    def __str__(self):
        return self.title




class Filmography(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Award(models.Model):
    title = models.CharField(max_length=200, default='Award Title')
    description = models.TextField(default='Description of the award.')
    year = models.DateField(default='2024-01-01')  # Default date example, adjust as needed

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to="media")
    song = models.FileField(upload_to="media")



    def __str__(self):
        return f'{self.title},{self.image},{self.song}'
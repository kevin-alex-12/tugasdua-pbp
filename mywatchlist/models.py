from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
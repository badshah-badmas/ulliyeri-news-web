import datetime

from django.db import models

# Create your models here.
from image_cropping import ImageRatioField


class BreakingNews(models.Model):
    heading = models.CharField(max_length=150)
    news = models.TextField()
    image = models.ImageField(upload_to='media/images')
    cropping = ImageRatioField('image', '1920x1080')
    def __str__(self):
        return str(self.pk)

class TrendingNews(models.Model):
    heading = models.CharField(max_length=150)
    news = models.TextField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return str(self.pk)

class LatestNews(models.Model):
    heading = models.CharField(max_length=150)
    news = models.TextField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return str(self.pk)

class Contact(models.Model):
    groupLink = models.TextField()
    contactLink = models.TextField()
    def __str__(self):
        return str(self.pk)

class HomePageBannerAds(models.Model):
    title = models.TextField()
    description = models.TextField()
    postDate = datetime.date.today()
    image = models.ImageField(upload_to='advertisement')



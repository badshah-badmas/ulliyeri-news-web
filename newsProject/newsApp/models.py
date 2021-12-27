import datetime

from django.db import models

# Create your models here.
from image_cropping import ImageRatioField


class BreakingNews(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=150)
    short_news = models.TextField()
    news = models.TextField()
    image = models.ImageField(upload_to='media/images')
    postDate = datetime.date.today()
    creator_type = models.CharField(max_length=50)
    creator_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


class TrendingNews(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=150)
    short_news = models.TextField()
    news = models.TextField()
    image = models.ImageField(upload_to='images')
    postDate = datetime.date.today()
    creator_type = models.CharField(max_length=50)
    creator_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


class LatestNews(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=150)
    short_news = models.TextField()
    news = models.TextField()
    image = models.ImageField(upload_to='images')
    postDate = datetime.date.today()
    creator_type = models.CharField(max_length=50)
    creator_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


class EntertainmentNews(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=150)
    short_news = models.TextField()
    news = models.TextField()
    image = models.ImageField(upload_to='images')
    postDate = datetime.date.today()
    creator_type = models.CharField(max_length=50)
    creator_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


class LocalNews(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=150)
    short_news = models.TextField()
    news = models.TextField()
    image = models.ImageField(upload_to='images')
    postDate = datetime.date.today()
    creator_type = models.CharField(max_length=50)
    creator_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


class EducationNews(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=150)
    short_news = models.TextField()
    news = models.TextField()
    image = models.ImageField(upload_to='images')
    postDate = datetime.date.today()
    creator_type = models.CharField(max_length=50)
    creator_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


class PoliticalNews(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=150)
    short_news = models.TextField()
    news = models.TextField()
    image = models.ImageField(upload_to='images')
    postDate = datetime.date.today()
    creator_type = models.CharField(max_length=50)
    creator_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk)


class Contact(models.Model):
    groupLink = models.TextField()
    contactLink = models.TextField()

    def __str__(self):
        return str(self.pk)


class HomePageBannerAds(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    postDate = datetime.date.today()
    image = models.ImageField(upload_to='advertisement')

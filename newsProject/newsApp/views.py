from datetime import datetime
from .models import BreakingNews, TrendingNews, LatestNews, HomePageBannerAds, Contact
from django.shortcuts import render


# Create your views here.


def home(request):
    date = datetime.now().date()
    day = datetime.now().strftime("%A").upper()
    breaking_news_list = BreakingNews.objects.all()
    trending_news_list = TrendingNews.objects.all()
    latest_news_list = LatestNews.objects.all()
    main_banner_ad = HomePageBannerAds.objects.all()
    cotext = {'date': date, 'day': day, 'breakingNewsList': breaking_news_list, 'trendingNewsList': trending_news_list,
              'latestNewsList': latest_news_list,'mainBannerAd':main_banner_ad}
    return render(request, 'homePage.html', cotext)


def sample(request):
    breaking_news_list = BreakingNews.objects.all()
    return render(request, 'test.html', {'breakingNewsList': breaking_news_list})

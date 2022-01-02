from datetime import datetime
from .models import BreakingNews, TrendingNews, LatestNews, EducationNews, LocalNews, PoliticalNews, HomePageBannerAds, \
    Contact, EntertainmentNews, Recipe, Obituary
from django.shortcuts import render


# Create your views here.

def page_not_found_view(request, exception):
    date = datetime.now().date()
    day = datetime.now().strftime("%A").upper()
    return render(request, 'pages/404.html', {'date': date, 'day': day}, status=404)


def home(request):
    date = datetime.now().date()
    day = datetime.now().strftime("%A").upper()
    breaking_news_list = BreakingNews.objects.all()
    trending_news_list = TrendingNews.objects.all()
    latest_news_list = LatestNews.objects.all()
    entertainment_news_list = EntertainmentNews.objects.all()
    recipe_list = Recipe.objects.all()
    main_banner_ad = HomePageBannerAds.objects.all()
    context = {'date': date, 'day': day, 'breakingNewsList': breaking_news_list, 'trendingNewsList': trending_news_list,
               'latestNewsList': latest_news_list, 'mainBannerAd': main_banner_ad,
               'entertainmentNewsList': entertainment_news_list, 'recipeList': recipe_list}
    return render(request, 'pages/homePage.html', context)


def category(request, category_name):
    date = datetime.now().date()
    day = datetime.now().strftime("%A").upper()
    main_banner_ad = HomePageBannerAds.objects.all()
    if category_name == 'latest':
        latest_news_list = LatestNews.objects.all()
        category_context = {'category': "LATEST", 'date': date, 'day': day, 'newsList': latest_news_list,
                            'mainBannerAd': main_banner_ad}
    elif category_name == 'trending':
        trending_news_list = TrendingNews.objects.all()
        category_context = {'category': "TRENDING", 'date': date, 'day': day, 'newsList': trending_news_list,
                            'mainBannerAd': main_banner_ad}
    elif category_name == 'entertainment':
        entertainment_news_list = EntertainmentNews.objects.all()
        category_context = {'category': "ENTERTAINMENT", 'date': date, 'day': day, 'newsList': entertainment_news_list,
                            'mainBannerAd': main_banner_ad}
    elif category_name == 'education':
        education_news_list = EducationNews.objects.all()
        category_context = {'category': "EDUCATION", 'date': date, 'day': day, 'newsList': education_news_list,
                            'mainBannerAd': main_banner_ad}
    elif category_name == 'political':
        political_news_list = PoliticalNews.objects.all()
        category_context = {'category': "POLITICAL", 'date': date, 'day': day, 'newsList': political_news_list,
                            'mainBannerAd': main_banner_ad}
    elif category_name == 'local':
        local_news_list = LocalNews.objects.all()
        category_context = {'category': "LOCAL", 'date': date, 'day': day, 'newsList': local_news_list,
                            'mainBannerAd': main_banner_ad}
    elif category_name == 'recipes':
        recipe_list = Recipe.objects.all()
        category_context = {'category': "RECIPES", 'date': date, 'day': day, 'newsList': recipe_list,
                            'mainBannerAd': main_banner_ad}
    elif category_name == 'obituary':
        obituary_list = Obituary.objects.all()
        category_context = {'category': "OBITUARY", 'date': date, 'day': day, 'newsList': obituary_list,
                            'mainBannerAd': main_banner_ad}
    else:
        return render(request, 'pages/404.html', {'date': date, 'day': day})
    return render(request, 'pages/category.html', category_context)


def details(request, category_name, news_id):
    date = datetime.now().date()
    day = datetime.now().strftime("%A").upper()
    main_banner_ad = HomePageBannerAds.objects.all()
    trending_news_list = TrendingNews.objects.all()
    if category_name == "breaking":
        news = BreakingNews.objects.get(id=news_id)
    if category_name == "latest":
        news = LatestNews.objects.get(id=news_id)
    if category_name == "trending":
        news = TrendingNews.objects.get(id=news_id)
    if category_name == "entertainment":
        news = EntertainmentNews.objects.get(id=news_id)
    if category_name == 'education':
        news = EducationNews.objects.get(id=news_id)
    if category_name == 'political':
        news = PoliticalNews.objects.get(id=news_id)
    if category_name == 'local':
        news = LocalNews.objects.get(id=news_id)
    if category_name == 'recipes':
        news = Recipe.objects.get(id=news_id)

    context = {'id': news_id, 'category': category_name, 'date': date, 'day': day, 'news': news,
               'trendingNewsList': trending_news_list, 'mainBannerAd': main_banner_ad}
    return render(request, 'pages/details.html', context)

from rest_framework import serializers
from .models import BreakingNews, TrendingNews, LatestNews, EntertainmentNews, EducationNews, \
    LocalNews, PoliticalNews, HomePageBannerAds, Contact


class BreakingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BreakingNews
        fields = ("id", "heading", "short_news", "news", "image", "postDate", "creator_type", "creator_id")

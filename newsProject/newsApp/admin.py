from django.contrib import admin
from .models import BreakingNews,TrendingNews,LatestNews,HomePageBannerAds,Contact

# Register your models here.


admin.site.register(BreakingNews,)
admin.site.register(TrendingNews)
admin.site.register(LatestNews)
admin.site.register(HomePageBannerAds)
admin.site.register(Contact)
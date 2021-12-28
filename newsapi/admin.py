from django.contrib import admin

# Register your models here.
from .models import BreakingNews,TrendingNews,LatestNews,EntertainmentNews,EducationNews,LocalNews,PoliticalNews,HomePageBannerAds,Contact

admin.site.register(BreakingNews,)
admin.site.register(TrendingNews)
admin.site.register(LatestNews)
admin.site.register(EntertainmentNews)
admin.site.register(EducationNews)
admin.site.register(LocalNews)
admin.site.register(PoliticalNews)
admin.site.register(HomePageBannerAds)
admin.site.register(Contact)
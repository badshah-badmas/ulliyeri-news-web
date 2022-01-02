from django.contrib import admin
from .models import BreakingNews,TrendingNews,LatestNews,EntertainmentNews,EducationNews,LocalNews,PoliticalNews ,HomePageBannerAds,Recipe,Obituary,Contact

# Register your models here.


admin.site.register(BreakingNews,)
admin.site.register(TrendingNews)
admin.site.register(LatestNews)
admin.site.register(EntertainmentNews)
admin.site.register(EducationNews)
admin.site.register(LocalNews)
admin.site.register(PoliticalNews)
admin.site.register(HomePageBannerAds)
admin.site.register(Contact)
admin.site.register(Recipe)
admin.site.register(Obituary)
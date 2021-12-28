from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category_name>/',views.category,name = 'category'),
    path('category/<str:category_name>/<int:news_id>/',views.details,name = 'details')
]
handler404 = "newsApp.views.page_not_found_view"
from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BreakingSerializer
from .models import BreakingNews


# Create your views here.


class BreakingViewSet(viewsets.ModelViewSet):
    queryset = BreakingNews.objects.all().order_by('id')
    serializer_class = BreakingSerializer


def home(request):
    date = datetime.now().date()
    day = datetime.now().strftime("%A").upper()
    cotext = {'date': date, 'day': day, }
    return render(request, 'homePage.html', cotext)

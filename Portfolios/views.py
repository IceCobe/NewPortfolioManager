from django.shortcuts import render
from django.http import HttpResponse

from Portfolios.models import *


def home(request):
    stocks = Stock.objects.all()
    return render(request, 'home.html', {'stocks':stocks})
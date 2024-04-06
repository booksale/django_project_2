from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def article_2023(request):
    return HttpResponse('<h1>Article 2023</h1>')
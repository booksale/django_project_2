from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def catalog(request):
    return HttpResponse('<h1>Catalog</h1>')

def index(request):
    return render(request, 'index.html')
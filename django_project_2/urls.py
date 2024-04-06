"""
URL configuration for django_project_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rules import views as views_1
from catalog import views as views_2
from articles import views as articles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/2023/', articles.article_2023, name='article_2023'),
    path('rules/', views_1.rules, name='rules'),
    path('catalog/', views_2.catalog, name='catalog'),
    path('', views_1.index, name='index')
]

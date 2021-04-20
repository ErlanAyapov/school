from django.urls import path  
from . import views


urlpatterns = [
    path('',  views.main, name = 'home'),
    path('add', views.ArticleAddView, name = 'add_news'),
]

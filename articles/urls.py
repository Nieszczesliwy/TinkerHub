from django.urls import path
from .views import *

urlpatterns = [
    path('', renderHomePage, name='homepage'),
    path('create_article/', createArticle, name='create_article'),
    path('single/<int:aID>', renderSingleArticle, name='create_article'),
]


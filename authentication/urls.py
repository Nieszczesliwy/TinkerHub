from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
    path('428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324', login_view, name='login_page'),
    path('00270cf63f93c307e7e9d2cc7e639fa50aca58eeb64be3266a798c9c19535219', logout_view, name='logout_page')
]

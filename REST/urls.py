from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.PersonView.as_view()),
    path('add/', views.WeatherViews.as_view()),
]

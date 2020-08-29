from django.urls import path
from . import views
from django.views.generic import DetailView
from .models import Animal
from django.conf.urls import url

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    url(r'animal/(?P<pk>\d+)/', DetailView.as_view(model=Animal), name='animal'),
]
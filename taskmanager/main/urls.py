from django.urls import path
from django.urls import re_path
from .import views


urlpatterns = [
    path('', views.main, name='home'),
    re_path(r'^aboutme', views.aboutme, name='aboutme'),
    re_path(r'^aboutme2', views.aboutme2, name='aboutme2'),
    re_path(r'^aboutme3', views.aboutme3, name='aboutme3'),
    re_path(r'^works', views.works, name='works'),
    re_path(r'^works2', views.works2, name='works2'),
    re_path(r'^order', views.order, name='order'),
    re_path(r'^reviews', views.reviews, name='reviews'),
    re_path(r'^contact', views.contact, name='contact'),
    re_path(r'^main', views.main),
]
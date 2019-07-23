from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('list/', views.list, name='list'),
    path('start/', views.start, name='start'),
    path('search/', views.search, name='search'),
]

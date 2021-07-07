from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.galler, name='gallery'),
    path('add/', views.add, name='add'),
    path('photo/<str:pk>/', views.photo, name='photo'),
    path('delete/<str:pk>/', views.viewdelete.as_view(), name='delete'),

]
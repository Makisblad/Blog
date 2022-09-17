from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', Posts_By_Category.as_view(), name='category'),
    path('post/<str:slug>/', Single_Post.as_view(), name='post'),
    path('tag/<str:slug>/', Posts_By_Tag.as_view(), name='tag'),
    path('search/',Search.as_view(),name='search'),


]
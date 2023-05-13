from manga import views
from django.urls import re_path
from django.urls import path



urlpatterns = [
    path('mangas/<int:pk>/', views.MangaDetailView.as_view()),
    path('mangas/', views.MangaListView.as_view()),   
]


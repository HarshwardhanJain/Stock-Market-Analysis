from django.urls import path
from . import views

urlpatterns = [
    path('categories/<str:category>/queries/', views.list_queries),
    path('categories/<str:category>/queries/<str:filename>/', views.get_query),
    path('categories/<str:category>/output/<str:filename>/', views.get_output),
]

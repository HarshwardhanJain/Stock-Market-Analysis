from django.contrib import admin
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/<str:category>/queries/', views.list_queries),
    path('api/categories/<str:category>/queries/<str:filename>/', views.get_query),
    path('api/categories/<str:category>/output/<str:filename>/', views.get_output_csv),

    # Now using the cleaner views.serve_visualization
    re_path(r'^api/categories/(?P<category>[^/]+)/visualization/(?P<filename>[^/]+\.png)$', views.serve_visualization),
]

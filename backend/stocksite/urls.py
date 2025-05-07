from django.contrib import admin
from django.urls import path
from api import views  # 👈 pulls the 3 API views from views.py

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Lists all .txt Hive queries in a category
    path('api/categories/<str:category>/queries/', views.list_queries),

    # ✅ Loads a specific Hive query .txt file content
    path('api/categories/<str:category>/queries/<str:filename>/', views.get_query),

    # ✅ Loads a specific .csv result if present
    path('api/categories/<str:category>/output/<str:filename>/', views.get_output_csv),
]

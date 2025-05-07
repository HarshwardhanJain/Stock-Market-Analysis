import os
import pandas as pd
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_queries(request, category):
    folder = os.path.join(settings.PROJECT_DATA_ROOT, category)
    try:
        files = [f for f in os.listdir(folder) if f.endswith('.txt')]
        return JsonResponse({'files': files})
    except FileNotFoundError:
        return JsonResponse({'error': 'Category not found'}, status=404)

@api_view(['GET'])
def get_query(request, category, filename):
    file_path = os.path.join(settings.PROJECT_DATA_ROOT, category, filename)
    if not os.path.exists(file_path):
        return JsonResponse({'error': 'File not found'}, status=404)
    with open(file_path, 'r') as f:
        content = f.read()
    return JsonResponse({'filename': filename, 'content': content})

@api_view(['GET'])
def get_output(request, category, filename):
    csv_file = os.path.join(settings.PROJECT_DATA_ROOT, category, 'output', filename.replace('.txt', '.csv'))
    if not os.path.exists(csv_file):
        return JsonResponse({'error': 'CSV not found'}, status=404)
    df = pd.read_csv(csv_file)
    return JsonResponse({'columns': list(df.columns), 'rows': df.to_dict(orient='records')})

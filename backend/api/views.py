import os
import urllib.parse
from django.conf import settings
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
import pandas as pd

@api_view(['GET'])
def list_queries(request, category):
    decoded_category = urllib.parse.unquote(category)
    folder = os.path.join(settings.PROJECT_DATA_ROOT, decoded_category)

    if not os.path.exists(folder):
        return JsonResponse({'files': []})

    files = [f for f in os.listdir(folder) if f.lower().endswith('.txt')]
    return JsonResponse({'files': sorted(files)})

@api_view(['GET'])
def get_query(request, category, filename):
    decoded_category = urllib.parse.unquote(category)
    decoded_filename = urllib.parse.unquote(filename)
    file_path = os.path.join(settings.PROJECT_DATA_ROOT, decoded_category, decoded_filename)

    if not os.path.exists(file_path):
        raise Http404("Query file not found.")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return JsonResponse({'content': content})

@api_view(['GET'])
def get_output_csv(request, category, filename):
    decoded_category = urllib.parse.unquote(category)
    decoded_filename = urllib.parse.unquote(filename)
    csv_name = decoded_filename.replace('.txt', '.csv')
    output_path = os.path.join(settings.PROJECT_DATA_ROOT, decoded_category, 'output', csv_name)

    if not os.path.exists(output_path):
        return JsonResponse({'error': 'CSV not found'}, status=404)

    try:
        df = pd.read_csv(output_path)
    except Exception:
        return JsonResponse({'error': 'Failed to read CSV'}, status=500)

    return JsonResponse({
        'columns': list(df.columns),
        'rows': df.to_dict(orient='records')
    })

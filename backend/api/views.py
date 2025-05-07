import os
import urllib.parse
from django.conf import settings
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
import pandas as pd

@api_view(['GET'])
def list_queries(request, category):
    import urllib.parse
    import os
    from django.conf import settings
    from django.http import JsonResponse

    decoded_category = urllib.parse.unquote(category)
    folder = os.path.join(settings.PROJECT_DATA_ROOT, decoded_category)

    # ✅ Add debug statements below
    print("\n=== DEBUG: Hive Query List ===")
    print("Raw category:", category)
    print("Decoded category:", decoded_category)
    print("Full path:", folder)
    print("Path exists:", os.path.exists(folder))
    if os.path.exists(folder):
        print("Files in folder:", os.listdir(folder))

    if not os.path.exists(folder):
        print("❌ Folder not found")
        return JsonResponse({'files': []})

    try:
        all_files = os.listdir(folder)
        print("🗂 Files in folder:", all_files)

        txt_files = [f for f in all_files if f.lower().endswith('.txt')]
        print("✅ Returning TXT files:", txt_files)
        return JsonResponse({'files': sorted(txt_files)})
    except Exception as e:
        print("❌ Exception:", str(e))
        return JsonResponse({'files': [], 'error': str(e)}, status=500)

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

    base_name = decoded_filename.replace('.txt', '')
    output_folder = os.path.join(settings.PROJECT_DATA_ROOT, decoded_category, 'output')
    csv_path = os.path.join(output_folder, base_name + '.csv')
    txt_path = os.path.join(output_folder, base_name + '.txt')

    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)
            return JsonResponse({
                'columns': list(df.columns),
                'rows': df.to_dict(orient='records')
            })
        except Exception:
            return JsonResponse({'error': 'Failed to parse CSV'}, status=500)

    elif os.path.exists(txt_path):
        with open(txt_path, 'r', encoding='utf-8') as f:
            return JsonResponse({'txt': f.read()})

    return JsonResponse({'error': 'No output file found'}, status=404)

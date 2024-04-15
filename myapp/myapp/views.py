from django.http import JsonResponse
from django.shortcuts import render
import requests

def fetch(request):
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data, safe=False)
        # render(request, 'template.html', {'posts': data})
    except requests.exceptions.RequestException as e:
            return JsonResponse({'error':str(e)}, status = 500)
from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    data = {}
    try:
        data = json.loads(request.body)
    except Exception as e:
        print(e)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse({"message": "Hello, World"})

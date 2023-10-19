from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.


@csrf_exempt
def route_test(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # get query params
        query_params = request.GET

        return JsonResponse({
            "method": request.method,
            "path": request.path,
            "query_params": dict(query_params),
        }, safe=False)

    elif request.method == 'POST':
        # get body
        body = request.body.decode("utf-8")
        # parse json
        parsed_body = json.loads(body)

        return JsonResponse({
            "method": request.method,
            "path": request.path,
            "body": body,
            "parsed_body": parsed_body,
        }, status=201)

    else:
        return JsonResponse({
            "method": request.method,
            "path": request.path,
        }, status=405)

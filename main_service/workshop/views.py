from django.http import JsonResponse

def healthy(request):
    data = {'message': 'OK.'}
    return JsonResponse(data)
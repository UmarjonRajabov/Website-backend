from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from asosiy.models import Asosiy
from asosiy.serializers import AsosiySerializer 


@csrf_exempt
def asosiy_list(request):
    """
    List all code numbers, or create a new number.
    """
    if request.method == 'GET':
        asosiy = Asosiy.objects.all()
        serializer = AsosiySerializer(asosiy, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AsosiySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def asosiy_detail(request, pk):
    """
    Retrieve a number.
    """
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
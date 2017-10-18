from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from activitys.models import Activity
from rest_framework import viewsets
from contacts.serializers import activitysSerializer, Activitys_list_Serializer


# Create your views here.
class activitysViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = activitysSerializer

@csrf_exempt
def activitys_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        all_list = Activity.objects.all()
        serializer = Activitys_list_Serializer(all_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = activitysSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def activitys_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Activity.objects.get(id=pk)
    except Activity.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Activitys_list_Serializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = activitysSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Activity.delete()
        return HttpResponse(status=204)

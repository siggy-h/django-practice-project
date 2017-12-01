from django.shortcuts import render
from django.http import JsonResponse


def myapp_home(request):
    return JsonResponse({'foo':'bar'})

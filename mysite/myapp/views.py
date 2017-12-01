from django.shortcuts import render
from django.http import JsonResponse

from myapp.models import MyModel


def myapp_home(request):

    names = MyModel.objects.all()

    return JsonResponse({'names': [name.my_name for name in names]})

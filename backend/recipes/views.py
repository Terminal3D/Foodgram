from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse
import os


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return HttpResponse("<h1>hello</h1>")
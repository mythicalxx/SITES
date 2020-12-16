from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world from Django, Gunicorn, Docker and NGINX")
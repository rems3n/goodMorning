# goodMornning/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is your new Django app.")

def page2(request):
    return HttpResponse("This is the second page.")

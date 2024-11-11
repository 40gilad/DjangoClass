from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello world! This is my first django hompage")

def about(request):
    return HttpResponse("This is my about page")
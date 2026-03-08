from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Daniel Vance Says Hello!")
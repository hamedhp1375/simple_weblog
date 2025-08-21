from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("سلام! این صفحه اصلی است.")

def about(request):
    return HttpResponse("این صفحه درباره ماست.")

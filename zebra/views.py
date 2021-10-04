from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def edc(request):
    return render(request, "edc/index.html")


def sample(request):
    return render(request, "sample/index.html")

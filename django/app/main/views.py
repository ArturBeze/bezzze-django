from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("<h4>main</h4>")

def about(request):
    return HttpResponse("<h4>about</h4>")

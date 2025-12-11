from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("<h4>main</h4>")

def help(request):
    return HttpResponse("<h4>help</h4>")

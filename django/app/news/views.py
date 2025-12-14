from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main():
    return HttpResponse("<h4>main</h4>")

def about():
    return HttpResponse("<h4>about</h4>")
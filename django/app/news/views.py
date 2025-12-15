from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("<h4>news</h4>")

def foo(request):
    return HttpResponse("<h4>foo</h4>")

def bar(request):
    return HttpResponse("<h4>bar</h4>")

def baz(request):
    return HttpResponse("<h4>baz</h4>")
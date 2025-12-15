from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache

# Create your views here.
def news_main(request):
    return render(request, 'news/index.html')

def foo(request):
    return HttpResponse("<h4>foo</h4>")

def bar(request):
    return HttpResponse("<h4>bar</h4>")

def baz(request):
    return HttpResponse("<h4>baz</h4>")
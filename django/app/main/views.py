from django.shortcuts import render
from django.http import HttpResponse
from .utils.online_users import get_online_users_count

# Create your views here.
def main(request):
    data = {'amount': get_online_users_count()}
    return render(request, 'main/index.html', data)

def about(request):
    # return HttpResponse("<h4>about</h4>")
    return render(request, "main/about.html")


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<html><body>Hello, World!</body></html>')

def about(request):
    return HttpResponse(
        "Here is the About Page. Go back home? <a href='/'>Home</a>"
    )

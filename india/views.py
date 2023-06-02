from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sehwag_string(request):
    return HttpResponse('<center><h1>This is <span style="color:red">Virendra Shehwag</span> Page</h1></center>')

def sehwag(request):
    return render(request, 'sehwag.html')

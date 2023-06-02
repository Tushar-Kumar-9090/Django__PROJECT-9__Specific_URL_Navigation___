from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat_strings(request):
    return HttpResponse('<center><h1>This is <span style="color:red">Virat Kohli</span> Page</h1></center>')

def virat(request):
    return render(request, 'virat.html')


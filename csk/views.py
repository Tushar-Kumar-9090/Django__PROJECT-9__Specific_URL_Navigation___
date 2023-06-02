from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def dhoni_strings(request):
    return HttpResponse('<center><h1>This is <span style="color:blue">M.S Dhoni</span> Page</h1></center>')

def dhoni(request):
    return render(request, 'dhoni.html')
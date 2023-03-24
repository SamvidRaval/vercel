from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# classes and function which are mapped to urls over here
def index(request):
    return render(request,'base.html',{})


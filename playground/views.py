from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate():
    x = 1
    y = 2 
    return x+y

# Creating a view function say_hello which will return response and print Hello world when someone accesses playground/hello page
def say_hello(request):
    x = calculate()
    return render(request,'hello.html', {'name':x})
from django.shortcuts import render

def index(request):
    print "Hello World"
    return render(request,'HelloWorld/index.html')
# Create your views here.

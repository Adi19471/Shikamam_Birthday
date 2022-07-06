from django.shortcuts import render

# Create your views here.


def home(request):
 
 return render(request, 'S/home.html')



def about(request):
 return render(request, 'S/about.html')


def mam(request):
 return render(request, 'S/mam.html')
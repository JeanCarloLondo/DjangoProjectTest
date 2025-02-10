from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   # return HttpResponse('<h1>Welcome to Home page<h1>')
   #return render(request, 'home.html')
   return render(request, 'home.html', {'name': 'Jean Carlo Londoño Ocampo'})

def about(request):
   # return HttpResponse('<h1>This is the "about" section<h1>')
   return render(request, 'about.html')
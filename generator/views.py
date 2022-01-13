from django.http.response import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def generator(request):
    return render(request, 
                  "generator/generator.html",
                  {"password": "carozum64"})

def contact(request):
    return HttpResponse("<h1>Hello I am the CONTACT page</h1>")   

def password(request):
    thepassword = ''
    length = int(request.GET.get('length', 12))
    characters = list("abcdefghijklmnopqrstuvwxyz")
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))
    
    if request.GET.get('specials'):
        characters.extend(list("&@#+/?=£%$*"))
    
    for _ in range(length):
        thepassword += random.choice(characters)
                           
    return render(request, 'generator/password.html', {'password': thepassword}
                  )
    
def about(request):
    return render(request, 'generator/about.html')
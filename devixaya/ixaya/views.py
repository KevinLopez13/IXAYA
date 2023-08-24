from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import math
# Create your views here.

def inicio(request):
    
    pat_query = Patrocinador.objects.all()
    patrocinadores = [pat_query[i*3:i*3+3] for i in range(math.ceil(len(pat_query)/3))]

    noticias =[
        {'title':'Tema 1','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'},
        {'title':'Tema 2','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'},
        {'title':'Tema 3','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'}
    ]

    return render(request,'inicio.html',{'patrocinadores':patrocinadores,'noticias':noticias})

def blog(request):
    
    entries_query = Blogpost.objects.all()
    #entries_by_pages = [entries_query[i*6:i*6+6] for i in range(math.ceil(len(entries_query)/6))]
    #pages = {i:f'P{i}' for i in range(1,len(entries_by_pages)+1)}
    print(entries_query[0].image.url)
    return render(request,'blog.html',{'posts':entries_query})

def blogpost(request, post):
    post = Blogpost.objects.get(title=post)
    return render(request, 'blogpost.html', {'post':post})
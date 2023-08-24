from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def inicio(request):
    patrocinadores = [
        [{'name':'Patrocinador 4', 'desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'},
        {'name':'Patrocinador 5', 'desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'},
        {'name':'Patrocinador 6', 'desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'}],
        [{'name':'Patrocinador 1', 'desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'},
        {'name':'Patrocinador 2', 'desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'},
        {'name':'Patrocinador 3', 'desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'}],
    ]
    noticias =[
        [
            {'title':'Tema 1','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'},
            {'title':'Tema 2','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'},
            {'title':'Tema 3','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'}
        ],
        [
            {'title':'Tema 4','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'},
            {'title':'Tema 5','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'},
            {'title':'Tema 6','desc':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'ref':'https://www.google.com', 'img':'../static/img/Satélite.svg'}
        ],
    ]
    return render(request,'inicio.html',{'patrocinadores':patrocinadores,'noticias':noticias})

def blog(request):
    return render(request,'blog.html')
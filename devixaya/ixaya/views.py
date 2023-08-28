from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import math
# Create your views here.

def inicio(request):
    
    pat_query = Patrocinador.objects.all()
    #patrocinadores = [pat_query[i*3:i*3+3] for i in range(math.ceil(len(pat_query)/3))]
    carousel_query = CarruselItem.objects.filter()

    return render(request,'inicio.html',
                  {
                    'sponsors':pat_query,
                    'carouselItems':carousel_query,
                   }
                )

def blog(request,page):
    ppp = 6 #post per page
    mpi = 5 # max per items
    ki = page*ppp
    posts_query = Blogpost.objects.all().order_by('-datetime')
    posts = posts_query[ki-ppp:ki]
    total_pages = math.ceil(len(posts_query)/ppp)
    pages = [p for p in range(1,total_pages+1) if page-mpi//2 <= p <= page+mpi//2]

    return render(request,'blog.html',
                  {'posts':posts,
                   'pages':pages,
                   'active':page,
                   'total_pages':total_pages,
                   'prev': page-1,
                   'next': page+1,
                   })

def blogpost(request, post):
    post = Blogpost.objects.get(title=post)
    return render(request, 'blogpost.html', {'post':post})

def support(request):
    return render(request, 'support.html')
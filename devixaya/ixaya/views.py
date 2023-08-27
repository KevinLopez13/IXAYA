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
    ki = page*6
    posts_query = Blogpost.objects.all().order_by('-datetime')[ki:ki+6]
    return render(request,'blog.html',{'posts':posts_query})

def blogpost(request, post):
    post = Blogpost.objects.get(title=post)
    return render(request, 'blogpost.html', {'post':post})

def support(request):
    return render(request, 'support.html')
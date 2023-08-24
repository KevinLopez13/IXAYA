from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('inicio', views.inicio, name='inicio' ),
    path('blog', views.blog, name='blog' ),
    path('blogpost/<post>', views.blogpost ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
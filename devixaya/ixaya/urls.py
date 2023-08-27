from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('inicio', views.inicio, name='inicio' ),
    path('blog/<int:page>', views.blog, name='blog' ),
    path('blogpost/<post>', views.blogpost ),
    path('support', views.support),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
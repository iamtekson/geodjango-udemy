from django.urls import path
from .views import index, jamoat

urlpatterns = [
    path('', index, name='index'),
    path('jamoatdata', jamoat, name='jamoatdata'),
]

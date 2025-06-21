from django.urls import path
from galeria.views import index, image, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', image, name='imagem'),
    path('buscar', buscar, name='buscar'),
]
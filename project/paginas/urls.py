from django.urls import path
from .views import PaginaInicial

urlpatterns = [
    #path(endereco, qual_sera_a_view, nome_para_url)
    path('inicio/', PaginaInicial.as_view(), name='inicio')
]

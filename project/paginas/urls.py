from django.urls import path
from .views import IndexView

urlpatterns = [
    #path(endereco, qual_sera_a_view, nome_para_url)
    path('inicio/', IndexView.as_view(), name='inicio')
]

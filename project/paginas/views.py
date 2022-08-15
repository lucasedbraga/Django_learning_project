from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    # Classe para página inicial
    template_name= "paginas/index.html"

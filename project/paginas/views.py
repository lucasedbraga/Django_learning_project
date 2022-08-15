from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    # Classe para página inicial
    template_name= "paginas/modelo.html"

class SobreView(TemplateView):
    template_name= 'paginas/sobre.html'
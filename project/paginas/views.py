from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    # Classe para página inicial
    template_name= "index.html"

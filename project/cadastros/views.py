from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Campo, Atividade
from django.urls import reverse_lazy

#CreateView é mais utilizado para formularios
class CampoCreate(CreateView):
    model = Campo
    fields = ['nome','descricao']
    template_name =  'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index') 

###### UPDATE
class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome','descricao']
    template_name =  'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index') 

###### DELETE
class CampoDelete(DeleteView):
    model = Campo
    template_name =  'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name =  'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')


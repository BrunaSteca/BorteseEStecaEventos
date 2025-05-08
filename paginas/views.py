from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import TipoEvento, LocalizacaoEvento, Perfil, Funcionario, Evento, Orcamento
from django.urls import reverse_lazy

class Inicio(TemplateView):
    template_name = "paginas/index.html"
    
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'   

class TipoEventoCreate(CreateView):
    template_name = 'pagina/form.html'
    model = TipoEvento
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Tipo De Evento'}

class LocalizacaoCreate(CreateView):
    template_name = 'pagina/form.html'
    model = LocalizacaoEvento
    fields = ['nome' , 'endereco']
    success_url = reverse_lazy('sobre')
    extra_context = {'titulo' : 'Cadastrar Localização'}
 
class PerfilCreate(CreateView):
    template_name = 'pagina/form.html'
    model = Perfil
    fields = ['nome','cpf','telefone', 'endereco']
    success_url = reverse_lazy('sobre')
    extra_context = {'titulo' : 'Cadastrar Perfil'}

class FuncionarioCreate(CreateView):
    template_name = 'pagina/form.html'
    model = Funcionario
    fields = ['nome','cargo']
    success_url = reverse_lazy('sobre')
    extra_context = {'titulo' : 'Cadastrar Funcionario'}

class EventoCreate(CreateView):
    template_name = 'pagina/form.html'
    model = Evento
    fields = ['nome','tipoEvento', 'dataEvento']
    success_url = reverse_lazy('sobre')
    extra_context = {'titulo' : 'Cadastrar Evento'}


class OrcamentoCreate(CreateView):
    template_name = 'pagina/form.html'
    model = Orcamento
    fields = ['valorPrevisto','valorReal', 'despesas']
    success_url = reverse_lazy('sobre')
    extra_context = {'titulo' : 'Cadastrar Evento'}
 
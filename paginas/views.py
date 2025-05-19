from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import TipoEvento, LocalizacaoEvento, Perfil, Funcionario, Evento, Orcamento
from django.urls import reverse_lazy

class Inicio(TemplateView):
    template_name = "paginas/index.html"
    
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'   

class TipoEventoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = TipoEvento
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Tipo De Evento',
                     'botão' : 'Cadastrar',}

class LocalizacaoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = LocalizacaoEvento
    fields = ['nome' , 'endereco', 'capacidade_maxima']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Localização',
                     'botão' : 'Cadastrar',}
 
class PerfilCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Perfil
    fields = ['nome','cpf','telefone', 'endereco']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Perfil',
                     'botão' : 'Cadastrar',}

class FuncionarioCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Funcionario
    fields = ['nome','cargo']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Funcionario',
                     'botão' : 'Cadastrar',}

class EventoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Evento
    fields = ['nome','tipo_evento', 'data_evento', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Evento',
                     'botão' : 'Cadastrar',}


class OrcamentoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Orcamento
    fields = ['valor_previsto','valor_real', 'despesas', 'evento', 'concluido']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Evento',
                     'botão' : 'Cadastrar',}
    

    ##################################################################################


class TipoEventoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = TipoEvento
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar o Tipo de Evento',
                     'botão' : 'Editar',}
    
class LocalizacaoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = LocalizacaoEvento
    fields = ['nome' , 'endereco', 'capacidade_maxima']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Localização',
                     'botão' : 'Editar',}
 
    
class PerfilUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Perfil
    fields = ['nome','cpf','telefone', 'endereco']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Perfil',
                     'botão' : 'Editar',}
    
class FuncionarioUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Funcionario
    fields = ['nome','cargo']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Funcionario',
                     'botão' : 'Editar',}

class EventoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Evento
    fields = ['nome','tipo_evento', 'data_evento', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Evento',
                     'botão' : 'Editar',}
    
class OrcamentoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Orcamento
    fields = ['valor_previsto','valor_real', 'despesas', 'evento', 'concluido']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Evento',
                     'botão' : 'Editar',}

 #####################################################################
 
class TipoEventoDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = TipoEvento
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
class LocalizacaoDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = LocalizacaoEvento
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
    
class PerfilDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Perfil
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
class FuncionarioDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Funcionario
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
class EventoDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Evento
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
class OrcamentoDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Orcamento
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
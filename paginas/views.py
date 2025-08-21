from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import TipoEvento, LocalizacaoEvento, Perfil, Funcionario, Evento, Orcamento
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm


# Crie a view no final do arquivo ou em outro local que faça sentido
class CadastroUsuarioView(CreateView):
    model = User
    # Não tem o fields, pois ele é definido no forms.py
    form_class = UsuarioCadastroForm
    # Pode utilizar o seu form padrão
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': 'Cadastro de Usuário',
        'botão': 'Registrar',
    }


    def form_valid(self, form):
        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Usuário ')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)
        # Retorna a URL de sucesso
        return url

#criação das listass


class Inicio(TemplateView):
    template_name = "paginas/index.html"
    
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'   

class TipoEventoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = TipoEvento
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Tipo De Evento',
                     'botão' : 'Cadastrar',}
    

class LocalizacaoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = LocalizacaoEvento
    fields = ['nome' , 'endereco', 'capacidade_maxima']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Localização',
                     'botão' : 'Cadastrar',}
    
 
class PerfilCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Perfil
    fields = ['nome','cpf','telefone', 'endereco']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Perfil',
                     'botão' : 'Cadastrar',}
    

class FuncionarioCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Funcionario
    fields = ['nome','cargo']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Funcionario',
                     'botão' : 'Cadastrar',}
    

class EventoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Evento
    fields = ['nome','tipo_evento', 'data_evento', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Evento',
                     'botão' : 'Cadastrar',}
    def form_valid(self,form):
        form.instance.cadastrado_por = self.request.user
        url = super().form_valid(form)
        return url

        


class OrcamentoCreate(LoginRequiredMixin, CreateView):
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
    success_url = reverse_lazy('listar')
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
    
#################################################################

class TipoEventoList(ListView):
    model = TipoEvento
    template_name = 'paginas/listas/tipo-evento.html'
    
class LocalizacaoList(ListView):
    model = LocalizacaoEvento
    template_name = 'paginas/listas/tipo-evento.html'

class PerfilList(ListView):
    model = Perfil
    template_name = 'paginas/listas/tipo-evento.html'

class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'paginas/listas/tipo-evento.html'

class EventoList(ListView):
    model = Evento
    template_name = 'paginas/listas/tipo-evento.html'

class OrcamentoList(ListView):
    model = Orcamento
    template_name = 'paginas/listas/tipo-evento.html'
    
############################################################################################################################################################

class TipoEventoList(LoginRequiredMixin, ListView):
    model = TipoEvento
    template_name = 'tipoEvento.html'


class LocalizacaoList(LoginRequiredMixin, ListView):
    model = LocalizacaoEvento
    template_name = 'localizacao.html'


class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = 'perfil.html'

class FuncionarioList(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'funcionario.html'

    
class EventoList(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'evento.html'

       
class OrcamentoList(LoginRequiredMixin, ListView):
    model = Orcamento
    template_name = 'orcamento.html'

#############################################################################################################################################################

class TipoEventoView(SuccessMessageMixin, CreateView):
    model = TipoEvento
    fields = ['nome']
    success_url = '/alunos/'
    success_message = "Tipo do evento criado com sucesso!"


class LocalizacaoView(SuccessMessageMixin, CreateView):
    model = LocalizacaoEvento
    fields = ['nome' , 'endereco', 'capacidade_maxima']
    success_url = '/alunos/'
    success_message = "Localização criada com sucesso!"


class PerfilView(SuccessMessageMixin, CreateView):
    model = Perfil
    fields = ['nome','cpf','telefone', 'endereco']
    success_url = '/alunos/'
    success_message = "Perfil criado com sucesso!"

class FuncionarioView(SuccessMessageMixin, CreateView):
    model = Funcionario
    fields = ['nome','cargo']
    success_url = '/alunos/'
    success_message = "Funcionario criado com sucesso!"

    
class EventoView(SuccessMessageMixin, CreateView):
    model = Evento
    fields = ['nome','cargo']
    success_url = '/alunos/'
    success_message = "Evento criado com sucesso!"

       
class OrcamentoView(SuccessMessageMixin, CreateView):
    model = Orcamento
    fields =  ['valor_previsto','valor_real', 'despesas', 'evento', 'concluido']
    success_url = '/alunos/'
    success_message = "Orçamento criado com sucesso!"



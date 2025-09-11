from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.models import TipoEvento, LocalizacaoEvento, Perfil, Funcionario, Evento, Orcamento
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioCadastroForm
from django.shortcuts import get_object_or_404



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
        'botao': 'Registrar',
    }


    def form_valid(self, form):
        nome = form.cleaned_data["nome"]
        telefone = form.cleaned_data["telefone"]

        # Faz o comportamento padrão do form_valid
        url = super().form_valid(form)
        # Busca ou cria um grupo com esse nome
        grupo, criado = Group.objects.get_or_create(name='Usuário')
        # Acessa o objeto criado e adiciona o usuário no grupo acima
        self.object.groups.add(grupo)

        # Criar um perfil pra esse usuário
        Perfil.objects.create(usuario = self.object, nome = nome, telefone = telefone)

        # Retorna a URL de sucesso
        return url

#criação das listass


class Inicio(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context["qtde_evento"] = Evento

        return context 
    
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'   

class TipoEventoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = TipoEvento
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Tipo De Evento',
                     'botao' : 'Cadastrar',}
    

class LocalizacaoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = LocalizacaoEvento
    fields = ['nome' , 'endereco', 'capacidade_maxima']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Localização', 
                     'botao' : 'Cadastrar',}
    
 
class PerfilCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Perfil
    fields = ['nome','cpf','telefone', 'endereco']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Perfil',
                     'botao' : 'Cadastrar',}
    

class FuncionarioCreate( GroupRequiredMixin, CreateView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Funcionario
    fields = ['nome','cargo', 'usuario']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Funcionario',
                     'botao' : 'Cadastrar',}
    

class EventoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginas/form.html'
    model = Evento
    fields = ['nome','tipo_evento', 'data_evento', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Evento',
                     'botao' : 'Cadastrar',}
    
    def form_valid(self,form):
        form.instance.cadastrado_por = self.request.user
        url = super().form_valid(form)
        return url

        


class OrcamentoCreate(GroupRequiredMixin, CreateView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Orcamento
    fields = ['valor_previsto','valor_real', 'despesas', 'evento', 'concluido']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Cadastrar Evento',
                     'botao' : 'Cadastrar',}
    

    ##################################################################################


class TipoEventoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = TipoEvento
    fields = ['nome']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar o Tipo de Evento',
                     'botao' : 'Editar',}
    
class LocalizacaoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = LocalizacaoEvento
    fields = ['nome' , 'endereco', 'capacidade_maxima']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Localização',
                     'botao' : 'Editar',}
 
    
class PerfilUpdate(GroupRequiredMixin,UpdateView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Perfil
    fields = ['nome','cpf','telefone', 'endereco']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Perfil',
                     'botao' : 'Editar',}
  
    
class FuncionarioUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Funcionario
    fields = ['nome','cargo', 'usuario']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Funcionario',
                     'botao' : 'Editar',}

class EventoUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Evento
    fields = ['nome','tipo_evento', 'data_evento', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Evento',
                     'botao' : 'Editar',}
   
    def get_object(self, queryset =None):
        obj = get_object_or_404(Evento, pk=self.kwargs['pk'], cadastrado_por=self.request.user)
        return obj


class OrcamentoUpdate(GroupRequiredMixin, UpdateView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Orcamento
    fields = ['valor_previsto','valor_real', 'despesas', 'evento', 'concluido']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : 'Editar Evento',
                     'botao' : 'Editar',}

 #####################################################################
 
class TipoEventoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form.html'
    model = TipoEvento
    success_url = reverse_lazy('listar')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
class LocalizacaoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'paginas/form.html'
    model = LocalizacaoEvento
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
    
class PerfilDelete( GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Perfil
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
    # def get_object(self, queryset =None):
    #     obj = get_object_or_404(Perfil, pk=self.kwargs['pk'], evento_por=self.request.user)
    #     return obj
class FuncionarioDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Funcionario
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
class EventoDelete(GroupRequiredMixin,DeleteView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Evento
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}

     #Alterar o metodo q busca o objeto pelo ID(get_object)
    def get_object(self, queryset =None):
    #get_object_or_404 - busca o objeto ou retorna 404
        obj = get_object_or_404(Evento, pk=self.kwargs['pk'], cadastrado_por=self.request.user)

        return obj

    
class OrcamentoDelete(GroupRequiredMixin, DeleteView):
    group_required = ["Administrador"]
    template_name = 'paginas/form.html'
    model = Orcamento
    success_url = reverse_lazy('index')
    extra_context = {'deletar':True, 'titulo': 'Deletar XXXX'}
    
#################################################################

# class TipoEventoList(ListView):
#     model = TipoEvento
#     template_name = 'paginas/listas/tipo-evento.html'
    
# class LocalizacaoList(ListView):
#     model = LocalizacaoEvento
#     template_name = 'paginas/listas/localizacao.html'

# class PerfilList(ListView):
#     model = Perfil
#     template_name = 'paginas/listas/tipo-evento.html'

# class FuncionarioList(ListView):
#     model = Funcionario
#     template_name = 'paginas/listas/tipo-evento.html'

# class EventoList(ListView):
#     model = Evento
#     template_name = 'paginas/listas/tipo-evento.html'

# class OrcamentoList(ListView):
#     model = Orcamento
#     template_name = 'paginas/listas/tipo-evento.html'
    
############################################################################################################################################################

class TipoEventoList(LoginRequiredMixin, ListView):
    model = TipoEvento
    template_name = 'paginas/listas/tipo-evento.html'


class LocalizacaoList(LoginRequiredMixin, ListView):
    model = LocalizacaoEvento
    template_name = 'paginas/listas/localizacao.html'


class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil
    template_name = 'paginas/listas/perfil.html'

class FuncionarioList(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'paginas/listas/funcionario.html'

    
class EventoList(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'paginas/listas/evento.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class MeuEvento(EventoList):
    
    def get_queryset(self):
       qs = Evento.objects.filter(cadastrado_por=self.request.user)
       return qs
    #Como fazer consultar/filtros no Django
    #Classe.objects.all() #Retorna todos os objetos
    #Classe.objects.filter(atributio=algum_valor, a2=v2)

       
class OrcamentoList(LoginRequiredMixin, ListView):
    model = Orcamento
    template_name = 'paginas/listas/orcamento.html'

#############################################################################################################################################################

# class TipoEventoView(SuccessMessageMixin, CreateView):
#     model = TipoEvento
#     fields = ['nome']
#     success_url = '/alunos/'
#     success_message = "Tipo do evento criado com sucesso!"


# class LocalizacaoView(SuccessMessageMixin, CreateView):
#     model = LocalizacaoEvento
#     fields = ['nome' , 'endereco', 'capacidade_maxima']
#     success_url = '/alunos/'
#     success_message = "Localização criada com sucesso!"


# class PerfilView(SuccessMessageMixin, CreateView):
#     model = Perfil
#     fields = ['nome','cpf','telefone', 'endereco']
#     success_url = '/alunos/'
#     success_message = "Perfil criado com sucesso!"

# class FuncionarioView(SuccessMessageMixin, CreateView):
#     model = Funcionario
#     fields = ['nome','cargo']
#     success_url = '/alunos/'
#     success_message = "Funcionario criado com sucesso!"

    
# class EventoView(SuccessMessageMixin, CreateView):
#     model = Evento
#     fields = ['nome','cargo']
#     success_url = '/alunos/'
#     success_message = "Evento criado com sucesso!"

       
# class OrcamentoView(SuccessMessageMixin, CreateView):
#     model = Orcamento
#     fields =  ['valor_previsto','valor_real', 'despesas', 'evento', 'concluido']
#     success_url = '/alunos/'
#     success_message = "Orçamento criado com sucesso!"



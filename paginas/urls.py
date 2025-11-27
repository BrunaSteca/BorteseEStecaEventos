from django.urls import path
from .views import Inicio, SobreView
from .views import TipoEventoCreate, LocalizacaoCreate, PerfilCreate, FuncionarioCreate, EventoCreate, OrcamentoCreate
from .views import TipoEventoUpdate, LocalizacaoUpdate, PerfilUpdate, FuncionarioUpdate, EventoUpdate, OrcamentoUpdate
from .views import TipoEventoDelete, LocalizacaoDelete, PerfilDelete, FuncionarioDelete, EventoDelete, OrcamentoDelete
from .views import TipoEventoList, LocalizacaoList, PerfilList, FuncionarioList, EventoList, OrcamentoList
from django.contrib.auth import views as auth_views
from .views import CadastroUsuarioView
from .views import MeuEvento
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Evento, Funcionario

# trecho de JavaScript simples — pode ser inserido em templates quando necessário:
# Exemplo de uso no template Django: {{ JS_SNIPPET|safe }}
JS_SNIPPET = """
<script>
	// JS adicionado dinamicamente pelo módulo paginas.urls
	console.log("JavaScript inserido: paginas.urls JS_SNIPPET carregado");
	// Função de utilidade rápida
	function pingServidor(){ console.log("ping"); }
</script>
"""

# view rápida para deletar evento via GET/POST e redirecionar para listagem
@login_required
def deletar_evento_fast(request, pk):
	# ...pode adicionar checagem de proprietário se necessário...
	evento = get_object_or_404(Evento, pk=pk)
	evento.delete()
	return redirect('listar-evento')

# view rápida para deletar funcionário via GET/POST e redirecionar para listagem
@login_required
def deletar_funcionario_fast(request, pk):
	# ...adicione verificação de permissão/dono se necessário...
	func = get_object_or_404(Funcionario, pk=pk)
	func.delete()
	return redirect('listar-funcionario')

urlpatterns = [

    #criar uma rota "registrar" cadastrar novos usuários

    
    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),
    #criar rota para página de login
   path("login/", auth_views.LoginView.as_view(
       template_name = 'paginas/form.html',
       extra_context = {'titulo' : 'Autenticação',
                         'botão' : 'Entrar',}
      
   ), name="login"),

    #criar rota para página de login
   path("senha/", auth_views.PasswordChangeView.as_view(
       template_name = 'paginas/form.html',
       extra_context = {'titulo' : 'Atualizar senha',
                         'botão' : 'Salvar',}
      
   ), name="senha"),

   #criar uma rota para logout
   path("sair/", auth_views.LogoutView.as_view(), name="logout"),


   path("", Inicio.as_view(), name="index"), #url para página inicial
   path("sobre/", SobreView.as_view(), name="sobre"),

   path('adicionar/tipo-evento', TipoEventoCreate.as_view(), name = "inserir-tipo"), 
   path('adicionar/localizacao-evento', LocalizacaoCreate.as_view(), name = 'inserir-localizacao'),
   #path('adicionar/perfil',PerfilCreate.as_view(), name = 'inserir-perfil'),
   path('adicionar/funcionario',FuncionarioCreate.as_view(), name = 'inserir-funcionario'),
   path('adicionar/evento',EventoCreate.as_view(), name = 'inserir-evento'),
   path('adicionar/orcamento',OrcamentoCreate.as_view(), name = 'inserir-orcamento'),
   


   path("editar/tipo-evento/<int:pk>/", TipoEventoUpdate.as_view(), name = "editar-tipo"), 
   path("editar/localizacao-evento/<int:pk>/", LocalizacaoUpdate.as_view(), name = 'editar-localizacao'),
   path("editar/perfil/<int:pk>/", PerfilUpdate.as_view(), name= 'editar-perfil'),
   path("editar/funcionario/<int:pk>/", FuncionarioUpdate.as_view(),  name = 'editar-funcionario'),
   path("editar/evento/<int:pk>/", EventoUpdate.as_view(), name = 'editar-evento'),
   path("editar/orcamento/<int:pk>/", OrcamentoUpdate.as_view(), name = 'editar-orcamento'),



   path("deletar/tipo-evento/<int:pk>/", TipoEventoDelete.as_view(), name = "deletar-tipo"), 
   path("deletar/localizacao-evento/<int:pk>/", LocalizacaoDelete.as_view(), name = 'deletar-localizacao'),
   path("deletar/perfil/<int:pk>/", PerfilDelete.as_view(), name= 'deletar-perfil'),
   path("deletar/funcionario/<int:pk>/", deletar_funcionario_fast,  name = 'deletar-funcionario'),
   path("deletar/evento/<int:pk>/", deletar_evento_fast, name = 'deletar-evento'),
   path("deletar/orcamento/<int:pk>/", OrcamentoDelete.as_view(), name = 'deletar-orcamento'),

   path("listar/tipo-evento/", TipoEventoList.as_view(), name = "listar-tipo-evento"),
   path("listar/localizacao-evento/", LocalizacaoList.as_view(), name ="listar-localizacao"),
   path("listar/perfil-evento/", PerfilList.as_view(), name ="listar-perfil"),
   path("listar/funcionario-evento/", FuncionarioList.as_view(), name ="listar-funcionario"),
   path("listar/evento/", EventoList.as_view(), name ="listar-evento"),
   path("listar/orcamento-evento/", OrcamentoList.as_view(), name ="listar-orcamento"),
   

   path("listar/meu-evento/", MeuEvento.as_view(), name="listar-meu-evento"),

   
   


 
]

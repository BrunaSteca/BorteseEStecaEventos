
from django.urls import path
from .views import Inicio, SobreView
from .views import TipoEventoCreate, LocalizacaoCreate, PerfilCreate, FuncionarioCreate, EventoCreate, OrcamentoCreate
from .views import TipoEventoUpdate, LocalizacaoUpdate, PerfilUpdate, FuncionarioUpdate, EventoUpdate, OrcamentoUpdate
from .views import TipoEventoDelete, LocalizacaoDelete, PerfilDelete, FuncionarioDelete, EventoDelete, OrcamentoDelete
from .views import TipoEventoList, LocalizacaoList, PerfilList, FuncionarioList, EventoList, OrcamentoList

urlpatterns = [
    
   path("", Inicio.as_view(), name="index"), #url para página inicial
   path("sobre/", SobreView.as_view(), name="sobre"),

   path('adicionar/tipo-evento', TipoEventoCreate.as_view(), name = "inserir-tipo"), 
   path('adicionar/localizacao-evento', LocalizacaoCreate.as_view(), name = 'inserir-localizacao'),
   path('adicionar/perfil',PerfilCreate.as_view(), name = 'inserir-perfil'),
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
   path("deletar/funcionario/<int:pk>/", FuncionarioDelete.as_view(),  name = 'deletar-funcionario'),
   path("deletar/evento/<int:pk>/", EventoDelete.as_view(), name = 'deletar-evento'),
   path("deletar/orcamento/<int:pk>/", OrcamentoDelete.as_view(), name = 'deletar-orcamento'),

   path("listar/tipo-evento/", TipoEventoList.as_view(), name = "listar-tipo-evento"),
   path("listar/localizacao-evento/", LocalizacaoList.as_view(), name ="listar-localizacao"),
   path("listar/perfil-evento/", PerfilList.as_view(), name ="listar-perfil"),
   path("listar/funcionario-evento/", FuncionarioList.as_view(), name ="listar-funcionario"),
   path("listar/evento/", EventoList.as_view(), name ="listar-evento"),
   path("listar/orcamento-evento/", OrcamentoList.as_view(), name ="listar-orcamento"),
   
   
   



]


from django.urls import path
from .views import Inicio, SobreView
from .views import TipoEventoCreate, LocalizacaoCreate, PerfilCreate, FuncionarioCreate, EventoCreate, OrcamentoCreate

from .views import TipoEventoUpdate, LocalizacaoUpdate, PerfilUpdate, FuncionarioUpdate, EventoUpdate, OrcamentoUpdate
urlpatterns = [
    
   path("", Inicio.as_view(), name="index"), #url para página inicial
   path("sobre/", SobreView.as_view(), name="sobre"),

   path('adicionar/TipoEvento', TipoEventoCreate.as_view(), name = "inserir-tipo"), 
   path('adicionar/LocalizacaoEvento', LocalizacaoCreate.as_view(), name = 'inserir-localizacao'),
   path('adicionar/Perfil',PerfilCreate.as_view(), name = 'inserir-perfil'),
   path('adicionar/Funcionario',FuncionarioCreate.as_view(), name = 'inserir-funcionario'),
   path('adicionar/Evento',EventoCreate.as_view(), name = 'inserir-evento'),
   path('adicionar/Orcamento',OrcamentoCreate.as_view(), name = 'inserir-orcamento'),



   path("editar/tipoEvento/<int:pk>/", TipoEventoUpdate.as_view(), name = "editar-tipo"), 
   path("editar/localizacao/<int:pk>/", LocalizacaoUpdate.as_view(), name = 'editar-localizacao'),
   path("editar/perfil/<int:pk>/", PerfilUpdate.as_view(), name= 'editar-perfil'),
   path("editar/funcionario/<int:pk>/", FuncionarioUpdate.as_view(),  name = 'editar-funcionario'),
   path("editar/evento/<int:pk>/", EventoUpdate.as_view(), name = 'editar-evento'),
   path("editar/orcamento/<int:pk>/", OrcamentoUpdate.as_view(), name = 'editar-orcamento'),


]

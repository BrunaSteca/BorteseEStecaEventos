
from django.urls import path
from .views import Inicio, SobreView
from .views import TipoEventoCreate, LocalizacaoCreate, PerfilCreate, FuncionarioCreate, EventoCreate, OrcamentoCreate

urlpatterns = [
   path("index/", Inicio.as_view(), name="index"), #url para página inicial
   path("sobre/", SobreView.as_view(), name="sobre"),

   path('adicionar/TipoEvento', TipoEventoCreate.as_view(), name = "inserir-tipo"), 
   path('adicionar/LocalizacaoEvento', LocalizacaoCreate.as_view(), name = 'inserir-localizacao'),
   path('adicionar/Perfil',PerfilCreate.as_view(), name = 'inserir-perfil'),
   path('adicionar/Perfil',FuncionarioCreate.as_view(), name = 'inserir-funcionario'),
   path('adicionar/Perfil',EventoCreate.as_view(), name = 'inserir-evento'),
   path('adicionar/Perfil',OrcamentoCreate.as_view(), name = 'inserir-orcamento'),

]

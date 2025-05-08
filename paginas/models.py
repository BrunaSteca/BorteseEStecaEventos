from django.db import models
#Todas as classes DEVEM ter herança de models.Model
# Create your models here.

#Cria suas classes
class TipoEvento(models.Model):
    #Definir os atributos
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"
       
       
class LocalizacaoEvento(models.Model):
    nome = models.CharField(max_length = 150)
    endereco = models.CharField(max_length = 250, verbose_name = "endereço")
    capacidadeMaxima = models.PositiveSmallIntegerField()
    #campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    
class Perfil(models.Model):
    nome = models.CharField(max_length = 150)
    cpf = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 100)
    endereco = models.CharField(max_length = 250, verbose_name = "endereço")

    #descricao = models.CharField(max_length=250)
class Funcionario(models.Model):
    nome = models.CharField(max_length = 150)
    cargo = models.CharField(max_length = 150) 

class Evento(models.Model):
    nome = models.CharField(max_length = 150)
    tipoEvento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT)
    dataEvento = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length = 250, verbose_name = "descrição")

class Orcamento(models.Model):
    valorPrevisto = models.DecimalField(max_digits=10,decimal_places=2)
    valorReal = models.DecimalField(max_digits=10,decimal_places=2)
    despesas = models.TextField()
    evento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT)

    concluido = models.BooleanField(default=False)

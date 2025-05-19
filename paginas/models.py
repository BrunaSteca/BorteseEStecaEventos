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
    capacidade_maxima = models.PositiveSmallIntegerField()
    #campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.nome}"
       
    
class Perfil(models.Model):
    nome = models.CharField(max_length = 150)
    cpf = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 100)
    endereco = models.CharField(max_length = 250, verbose_name = "endereço")
    def __str__(self):
        return f"{self.nome}"

    #descricao = models.CharField(max_length=250)
class Funcionario(models.Model):
    nome = models.CharField(max_length = 150)
    cargo = models.CharField(max_length = 150) 
    def __str__(self):
        return f"{self.nome}"

class Evento(models.Model):
    nome = models.CharField(max_length = 150)
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT)
    data_evento = models.DateTimeField()
    descricao = models.CharField(max_length = 250, verbose_name = "descrição")
    def __str__(self):
        return f"{self.nome}"

class Orcamento(models.Model):
    valor_previsto = models.DecimalField(max_digits=10,decimal_places=2)
    valor_real = models.DecimalField(max_digits=10,decimal_places=2)
    despesas = models.TextField()
    evento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.valor_previsto}"


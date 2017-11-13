from django.db import models
from django.utils import timezone

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=20)
    chefe = models.BooleanField("Chefe de Departamento", default=False)
    def __str__(self):
        return self.cpf

class Configuracao(models.Model):
    cpf = models.ForeignKey(Funcionario, related_name = 'Pessoa_Horario', null=False)
    dataHoraEntradaFunci = models.DateTimeField(blank = True, null=True)
    dataHoraSaidaFunci = models.DateTimeField(blank = True, null=True)
    
class Ponto(models.Model):
    cpf = models.ForeignKey(Funcionario, related_name = 'Pessoa_Ponto', null=False)
    nomeChefe = models.CharField(max_length=128)
    dataHoraEntradaPonto = models.DateTimeField()
    dataHoraSaidaPonto = models.DateTimeField()
    tipo = models.CharField(max_length=20)
    hora = models.DateTimeField(default=timezone.now)
    ipMaquina = models.CharField(max_length=100)
    status = models.CharField(max_length=30)
    justificativa = models.TextField()
    





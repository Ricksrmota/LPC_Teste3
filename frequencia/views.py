from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from frequencia.serializers import UserSerializer
from frequencia.serializers import FuncionarioSerializer
from frequencia.serializers import ConfiguracaoSerializer
from frequencia.serializers import PontoSerializer
from frequencia.models import Funcionario
from frequencia.models import Configuracao
from frequencia.models import Ponto

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class ConfiguracaoViewSet(viewsets.ModelViewSet):
    queryset = Configuracao.objects.all()
    serializer_class = ConfiguracaoSerializer    
class PontoViewSet(viewsets.ModelViewSet):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer
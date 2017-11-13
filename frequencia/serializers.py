from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from frequencia.models import Funcionario
from frequencia.models import Configuracao
from frequencia.models import Ponto


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('__all__')

class ConfiguracaoSerializer(serializers.HyperlinkedModelSerializer):
    #cpf = FuncionarioSerializer(many = False)
    class Meta:
        model = Configuracao
        fields = '__all__'

    #def create(self,dados):
        #dados_config = dados.pop('cpf')
        #u = Funcionario.objects.create(**dados_config)
        #c = Configuracao.objects.create(cpf=u,**dados)
        #return c

class PontoSerializer(serializers.HyperlinkedModelSerializer):
    #cpf = FuncionarioSerializer(many = False)
    class Meta:
        model = Ponto
        fields = '__all__'

    #def create(self,dados):
        #dados_config = dados.pop('cpf')
        #u = Funcionario.objects.create(**dados_config)
        #c = Configuracao.objects.create(cpf=u,**dados)
        #return c
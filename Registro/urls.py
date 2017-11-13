from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from frequencia.views import UserViewSet
from frequencia.views import FuncionarioViewSet
from frequencia.views import ConfiguracaoViewSet
from frequencia.views import PontoViewSet

router = routers.DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'configuracoes', ConfiguracaoViewSet)
router.register(r'pontos', PontoViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

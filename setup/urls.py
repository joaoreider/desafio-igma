from django.contrib import admin
from django.urls import path, include
from clientes.views import ClientesViewSet
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 

schema_view = get_schema_view(
   openapi.Info(
      title="Cadastro de clientes | IGMA",
      default_version='v1',
      description="Cadastra e lista os clientes inseridos. ",
      terms_of_service="#",
      contact=openapi.Contact(email="contato.joaopaulo14@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename= 'Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

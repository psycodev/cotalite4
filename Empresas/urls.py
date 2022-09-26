
#from Empresas.views import empresaListView
from django.urls import path
from Empresas.views import regEmp
from Empresas.views import listemp
from Empresas.views import listempbyid
from Empresas.views import resempre
from Empresas.views import eliminarempresa
from Empresas.views import updateemp


urlpatterns = [
        path('register/', regEmp, name='register'),
        path('listar/', listemp, name='listarEmp'),
        path('listarbyid/', listempbyid, name='listarEmpbyid'),
        path('crear/',resempre,name='datosNuevaEmp'),
        path('eliminar/<int:nit>', eliminarempresa, name='Eliminar'),
        path('modificar/',updateemp,name='Modificar'),
    ]

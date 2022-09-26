
#from Empresas.views import empresaListView
from django.urls import path
from Transacciones.views import restrans
from Transacciones.views import listtr
from Transacciones.views import listtrbyid
from Transacciones.views import regTrs
from Transacciones.views import eliminartr 
from Transacciones.views import updatetr 


urlpatterns = [
        path('register/', restrans, name='register'),
        path('listar/', listtr, name='listarEmp'),
        path('listarbyid/', listtrbyid, name='listartransbyid'),
        path('crear/',regTrs,name='datosNuevaTrans'),
        path('eliminar/<int:nit>', eliminartr, name='Eliminar'), 
        path('modificar/',updatetr,name='Modificar'), 
    ]

from django.shortcuts import render
from django.shortcuts import redirect
from Transacciones.forms import registrarTransaccion
from Transacciones.models import Transaccion

def restrans(request):
    return render(request, "crearTransaccion-Contalite.html")

def regTrs(request):
    if request.method == 'POST':
        form = registrarTransaccion(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =registrarTransaccion()    
    return render(request, "visualizarTransaccionContalite.html",{'form':form})

def listtr(request):
    empresas = Transaccion.objects.all()
    contexto = {'empresas':empresas}
    return render(request, "visualizarTransaccionContalite.html",contexto)

def listtrbyid(request):
    emp_id=request.POST['uscar-nit']
    empresas = Transaccion.objects.filter(emp_id=emp_id)
    contexto = {'empresas':empresas}
    return render(request, "visualizarTransaccionContalite.html",contexto)



def eliminartr(request,nit):
    record = Transaccion.objects.get(nit = nit)
    record.delete()
    return redirect ('http://127.0.0.1:8000/transacciones/listar/')

def updatetr(request, id_tr):
    tr = Transaccion.objects.get(id_tr=id_tr)
    if request.method == 'GET':
        form=registrarTransaccion(instance=tr)
    else:
        form=registrarTransaccion(request.POST, instance=tr)
        if form.is_valid():
            form.save()
            print("Modificacion exitosa")
        return redirect("http://127.0.0.1:8000/transacciones/listar/")
    return render(request, 'visualizarTransaccionContalite.html', {'form':form}) 


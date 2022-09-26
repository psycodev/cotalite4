from django.shortcuts import render,redirect
from Empresas.forms import registrarEmpresa
from Empresas.models import Empresa

def resempre(request):
    return render(request, "crearEmpresa-Contalite.html")

def regEmp(request):
    if request.method == 'POST':
        form = registrarEmpresa(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =registrarEmpresa()    
    return render(request, "visualizarEmpresa-Contalite.html",{'form':form})

def listemp(request):
    empresas = Empresa.objects.all()
    contexto = {'empresas':empresas}
    return render(request, "visualizarEmpresa-Contalite.html",contexto)

def listempbyid(request):
    emp_id=request.POST['intnit1']
    empresas = Empresa.objects.filter(emp_id=emp_id)
    contexto = {'empresas':empresas}
    return render(request, "visualizarEmpresa-Contalite.html",contexto)



def eliminarempresa(request,nit):
    record = Empresa.objects.get(nit = nit)
    record.delete()
    return redirect ('http://127.0.0.1:8000/empresas/listar/')

def updateemp(request, nit):
    emp = Empresa.objects.get(id=nit)
    if request.method == 'GET':
        form=registrarEmpresa(instance=emp)
    else:
        form=registrarEmpresa(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            print("Modificaicon exitosa")
        return redirect("http://127.0.0.1:8000/empresas/listar/")
    return render(request, 'visualizarEmpresa-Contalite.html', {'form':form}) 

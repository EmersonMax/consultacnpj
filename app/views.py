from django.shortcuts import render
from .services import  apicnpj
from .forms import CnpjForm
# Create your views here.
def home(request):
    if request.method == "POST":
        cnpj = request.POST["cnpj"]
        estado = request.POST["estado"]
        context ={
          'dados':   apicnpj(cnpj,estado),
          'form_cnpj': CnpjForm(),
           
           'consulta': 'yes',
          
        }
        '''if context['dados']['cnpj'] == '':
            messages.error(request,'Cnpj invalido')
            return render(request,'cnpj.html',context)
        else:
            messages.success(request,'Cnpj Consultado')
            return render(request,'cnpj.html',context)'''
    else:
         context ={
        
          'form_cnpj': CnpjForm(),

          'consulta':'no',
          
        }
    return render(request, 'home.html', context)
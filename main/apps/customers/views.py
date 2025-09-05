from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Contrato
from .forms import ContratoAddForm


class ListContrato(View):

    def get(self, request):

        contratos = Contrato.objects.all()
        context = {
            'contratos': contratos
        }
        return render(request, 'list_contrato.html', context)



class ContratoAdd(View):
    def get(self, request):
        form = ContratoAddForm()
        context = {
            'form': form,
            'page_title': "Adicionar novo contrato"
        }
        return render(request, 'add_contrato.html', context)
    
    def post(self, request):
        form = ContratoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Contrato cadastrado com Sucesso")
            return redirect('listcontrato')
        
        messages.error(request, f"Não foi possível cadastrar o contrato.")
        context = {
            'form': form,
            'page_title': "Adicionar novo contrato"
        }
        return render(request, 'add_contrato.html', context)
    
class ContratoEdit(View):

    def get(self, request, id):
       group = Contrato.objects.get(pk=id)
       form = ContratoAddForm(request.POST or None, request.FILES or None, instance=group)
       context = {
           "form": form,
           "page_title": "Editar contrato"
       }
       return render(request, 'edit_contrato.html', context)

    def post(self, request, id):
        group = Contrato.objects.get(pk=id)
        form = ContratoAddForm(request.POST or None, request.FILES or None, instance=group)
        print (form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, f"Contrato editado com sucesso!")
            return redirect('listcontrato')

        messages.error(request, f"Não foi possível editar esse contrato {form.errors}")
        return redirect('listcontrato')
    

class ContratoDelete(View):
    def get(self, request, id):
       contrato = Contrato.objects.get(pk=id)
       contrato_delete = contrato.delete()
       messages.success(request, f"Contrato excluído com sucesso!")
       return redirect('listcontrato')
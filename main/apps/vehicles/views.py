from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Veiculo
from .forms import VeiculoAddForm

class ListVeiculo(View):

    def get(self, request):

        veiculos = Veiculo.objects.all()
        context = {
            'veiculos': veiculos
        }
        return render(request, 'list_veiculo.html', context)
    

class VeiculoAdd(View):
    def get(self, request):
        form = VeiculoAddForm()
        context = {
            'form': form,
            'page_title': "Adicionar novo veículo"
        }
        return render(request, 'add_veiculo.html', context)
    
    def post(self, request):
        form = VeiculoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Veículo cadastrado com Sucesso")
            return redirect('listveiculo')
        
        messages.error(request, f"Não foi possível cadastrar o veiculo.")
        context = {
            'form': form,
            'page_title': "Adicionar novo veiculo"
        }
        return render(request, 'add_veiculo.html', context)


class VeiculoEdit(View):

    def get(self, request, id):
       group = Veiculo.objects.get(pk=id)
       form = VeiculoAddForm(request.POST or None, request.FILES or None, instance=group)
       context = {
           "form": form,
           "page_title": "Editar Veículo"
       }
       return render(request, 'edit_veiculo.html', context)

    def post(self, request, id):
        group = Veiculo.objects.get(pk=id)
        form = VeiculoAddForm(request.POST or None, request.FILES or None, instance=group)
        print (form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, f"Veículo editado com sucesso!")
            return redirect('listveiculo')

        messages.error(request, f"Não foi possível editar esse veículo {form.errors}")
        return redirect('listveiculo')
    


class VeiculoDelete(View):
    def get(self, request, id):
       veiculo = Veiculo.objects.get(pk=id)
       veiculo_delete = veiculo.delete()
       messages.success(request, f"Veículo excluído com sucesso!")
       return redirect('listveiculo')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from .models import TabelaPreco
from .forms import TablePriceAddform


@method_decorator(login_required(login_url='login'), name='dispatch')
class ListTablePrice(View):

    def get(self, request):

        tabeladeprecos = TabelaPreco.objects.all()
        context = {
             "page_title": "Tabela de preço",
            'tabeladeprecos': tabeladeprecos
        }
        return render(request, 'tableprice/list_tableprice.html', context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class TablePriceAdd(View):

    def get(self, request):
       form = TablePriceAddform()
       context = {
           "form": form,
           "page_title": "Adicionar Tabela de preço"
       }
       return render(request, 'tableprice/add_tableprice.html', context)

    def post(self, request):
        form = TablePriceAddform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Tabela de preço cadastrada com sucesso!")
            return redirect('listunidade')

        messages.error(request, f"Não foi possível cadastrar a tabela de preço")
        context = {
            'form': form,
            "page_title": "Adicionar Tabela de preço"
        }
        return render(request, 'tableprice/add_tableprice.html', context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class TablePriceEdit(View):

    def get(self, request, id):
       group = TabelaPreco.objects.get(pk=id)
       form = TablePriceAddform(request.POST or None, request.FILES or None, instance=group)
       context = {
           "form": form,
           "page_title": "Editar tabela de preço"
       }
       return render(request, 'tableprice/edit_tableprice.html', context)

    def post(self, request, id):
        group = TabelaPreco.objects.get(pk=id)
        form = TablePriceAddform(request.POST or None, request.FILES or None, instance=group)
        print (form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, f"Tabela de preço Editada com sucesso!")
            return redirect('listtableprice')

        messages.error(request, f"Não foi possível editar essa tabela de preço {form.errors}")
        return redirect('listtableprice')


@method_decorator(login_required(login_url='login'), name='dispatch')
class TablePriceDelete(View):
    def get(self, request, id):
       tableprice = TabelaPreco.objects.get(pk=id)
       tableprice_delete = tableprice.delete()
       messages.success(request, f"Tablea de preço excluída com sucesso!")
       return redirect('listtableprice')
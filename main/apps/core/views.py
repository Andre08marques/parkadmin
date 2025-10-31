from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from .models import Unidade, Patio, Vaga
from .forms import UnidadeAddform, PatioForm, VagaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Unidade Views
@method_decorator(login_required(login_url='login'), name='dispatch')
class ListUnidade(View):

    def get(self, request):

        unidades = Unidade.objects.all()
        context = {
            'unidades': unidades
        }
        return render(request, 'unidade/list_unidade.html', context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class UnidadeAdd(View):

    def get(self, request):
       form = UnidadeAddform()
       context = {
           "form": form,
           "page_title": "Adicionar unidade"
       }
       return render(request, 'unidade/add_unidade.html', context)

    def post(self, request):
        form = UnidadeAddform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Unidade cadastrado com sucesso!")
            return redirect('listunidade')

        messages.error(request, "Não foi possível cadastrar a unidade")
        context = {
            'form': form,
            "page_title": "Adicionar unidade"
        }
        return render(request, 'alunos/add_unidade.html', context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class UnidadeEdit(View):

    def get(self, request, id):
       group = Unidade.objects.get(pk=id)
       form = UnidadeAddform(request.POST or None, request.FILES or None, instance=group)
       context = {
           "form": form,
           "page_title": "Editar unidade"
       }
       return render(request, 'unidade/edit_unidade.html', context)

    def post(self, request, id):
        group = Unidade.objects.get(pk=id)
        form = UnidadeAddform(request.POST or None, request.FILES or None, instance=group)
        print (form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, "Unidade Editada com sucesso!")
            return redirect('listunidade')

        messages.error(request, f"Não foi possível editar essa unidade {form.errors}")
        return redirect('listunidade')


@method_decorator(login_required(login_url='login'), name='dispatch')
class UnidadeDelete(View):
    def get(self, request, id):
       unidade = Unidade.objects.get(pk=id)
       unidade.delete()
       messages.success(request, "Unidade excluída com sucesso!")
       return redirect('listunidade')


# Patio Views
class PatioListView(LoginRequiredMixin, ListView):
    model = Patio
    template_name = 'core/patio_list.html'
    context_object_name = 'patios'

class PatioCreateView(LoginRequiredMixin, CreateView):
    model = Patio
    form_class = PatioForm
    template_name = 'core/patio_form.html'
    success_url = reverse_lazy('patio_list')

class PatioUpdateView(LoginRequiredMixin, UpdateView):
    model = Patio
    form_class = PatioForm
    template_name = 'core/patio_form.html'
    success_url = reverse_lazy('patio_list')

class PatioDeleteView(LoginRequiredMixin, DeleteView):
    model = Patio
    template_name = 'core/patio_confirm_delete.html'
    success_url = reverse_lazy('patio_list')

# Vaga Views
class VagaListView(LoginRequiredMixin, ListView):
    model = Vaga
    template_name = 'core/vaga_list.html'
    context_object_name = 'vagas'

class VagaCreateView(LoginRequiredMixin, CreateView):
    model = Vaga
    form_class = VagaForm
    template_name = 'core/vaga_form.html'
    success_url = reverse_lazy('vaga_list')

class VagaUpdateView(LoginRequiredMixin, UpdateView):
    model = Vaga
    form_class = VagaForm
    template_name = 'core/vaga_form.html'
    success_url = reverse_lazy('vaga_list')

class VagaDeleteView(LoginRequiredMixin, DeleteView):
    model = Vaga
    template_name = 'core/vaga_confirm_delete.html'
    success_url = reverse_lazy('vaga_list')
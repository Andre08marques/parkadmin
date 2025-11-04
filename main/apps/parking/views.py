from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import TabelaPreco, TipoVeiculo, TipoCobranca, Preco
from .forms import TablePriceAddform


# TabelaPreco CRUD Views
class TabelaPrecoListView(ListView):
    model = TabelaPreco
    template_name = 'parking/tabela_preco/list.html'
    context_object_name = 'tabelas'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(unidade__nome__icontains=search)
            )
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class TabelaPrecoCreateView(CreateView):
    model = TabelaPreco
    template_name = 'parking/tabela_preco/form.html'
    fields = ['unidade', 'nome', 'ativa', 'data_inicio', 'data_fim']
    success_url = reverse_lazy('parking:tabelapreco_list')

class TabelaPrecoUpdateView(UpdateView):
    model = TabelaPreco
    template_name = 'parking/tabela_preco/form.html'
    fields = ['unidade', 'nome', 'ativa', 'data_inicio', 'data_fim']
    success_url = reverse_lazy('parking:tabelapreco_list')

class TabelaPrecoDeleteView(DeleteView):
    model = TabelaPreco
    template_name = 'parking/tabela_preco/delete.html'
    success_url = reverse_lazy('parking:tabelapreco_list')

# TipoVeiculo CRUD Views
class TipoVeiculoListView(ListView):
    model = TipoVeiculo
    template_name = 'parking/tipo_veiculo/list.html'
    context_object_name = 'tipos_veiculo'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(descricao__icontains=search)
            )
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class TipoVeiculoCreateView(CreateView):
    model = TipoVeiculo
    template_name = 'parking/tipo_veiculo/form.html'
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('parking:tipoveiculo_list')

class TipoVeiculoUpdateView(UpdateView):
    model = TipoVeiculo
    template_name = 'parking/tipo_veiculo/form.html'
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('parking:tipoveiculo_list')

class TipoVeiculoDeleteView(DeleteView):
    model = TipoVeiculo
    template_name = 'parking/tipo_veiculo/delete.html'
    success_url = reverse_lazy('parking:tipoveiculo_list')

# TipoCobranca CRUD Views
class TipoCobrancaListView(ListView):
    model = TipoCobranca
    template_name = 'parking/tipo_cobranca/list.html'
    context_object_name = 'tipos_cobranca'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(descricao__icontains=search)
            )
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class TipoCobrancaCreateView(CreateView):
    model = TipoCobranca
    template_name = 'parking/tipo_cobranca/form.html'
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('parking:tipocobranca_list')

class TipoCobrancaUpdateView(UpdateView):
    model = TipoCobranca
    template_name = 'parking/tipo_cobranca/form.html'
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('parking:tipocobranca_list')

class TipoCobrancaDeleteView(DeleteView):
    model = TipoCobranca
    template_name = 'parking/tipo_cobranca/delete.html'
    success_url = reverse_lazy('parking:tipocobranca_list')

# Preco CRUD Views
class PrecoListView(ListView):
    model = Preco
    template_name = 'parking/preco/list.html'
    context_object_name = 'precos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(tabela__nome__icontains=search) |
                Q(tipo_veiculo__nome__icontains=search) |
                Q(tipo_cobranca__nome__icontains=search)
            )
        return queryset.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class PrecoCreateView(CreateView):
    model = Preco
    template_name = 'parking/preco/form.html'
    fields = ['tabela', 'tipo_veiculo', 'tipo_cobranca', 'valor']
    success_url = reverse_lazy('parking:preco_list')

class PrecoUpdateView(UpdateView):
    model = Preco
    template_name = 'parking/preco/form.html'
    fields = ['tabela', 'tipo_veiculo', 'tipo_cobranca', 'valor']
    success_url = reverse_lazy('parking:preco_list')

class PrecoDeleteView(DeleteView):
    model = Preco
    template_name = 'parking/preco/delete.html'
    success_url = reverse_lazy('parking:preco_list')
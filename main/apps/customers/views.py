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

from django.forms import SlugField
from django.shortcuts import render
from pontocoleta.models import Pontocoletas
from django.http import HttpResponse
from datetime import date
import sys
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator
from django.shortcuts import get_object_or_404

from siscol.roles import Pontocoleta

@has_permission_decorator('cadastrar_produtos')
def add_pontocoleta(request):
    if request.method == "GET":
        pontocoletas = Pontocoletas.objects.all()
        return render(request, 'add_pontocoleta.html',{'pontocoletas': pontocoletas})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        telefone =request.POST.get('telefone')
        bairro =request.POST.get('bairro')

        pontocoleta = Pontocoletas(nome=nome, endereco=endereco, telefone=telefone, bairro=bairro)

        pontocoleta.save()
        messages.add_message(request, messages.SUCCESS, 'Ponto de Coleta cadastrado com sucesso!!!')
        return redirect(reverse('add_pontocoleta'))

@has_permission_decorator('cadastrar_produtos')
def excluir_pontocoleta(request, id):
    pontocoleta =get_object_or_404(Pontocoletas, id=id)
    pontocoleta.delete()
    messages.add_message(request, messages.SUCCESS, 'Ponto de Coleta excluido com sucesso!!!')
    return redirect(reverse('add_pontocoleta'))
from django.shortcuts import render, get_object_or_404
from .models import Atividade
from .forms import AtividadeForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def programacao_list(request):
    programacao = Atividade.objects.all()
    return render(request, 'programacao_list.html', {'programacao': programacao})

def programacao_detail(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    return render(request, 'programacao_detail.html', {'atividade': atividade})

def programacao_create(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('programacao_list'))
    else:
        form = AtividadeForm()

    return render(request, 'programacao_form.html', {'form': form})

def programacao_edit(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('programacao_detail', args=[atividade_id]))
    else:
        form = AtividadeForm(instance=atividade)

    return render(request, 'programacao_form.html', {'form': form})

def programacao_delete(request, atividade_id):
    atividade = get_object_or_404(Atividade, pk=atividade_id)
    atividade.delete()
    return HttpResponseRedirect(reverse('programacao_list'))
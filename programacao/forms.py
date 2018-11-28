from django.forms import ModelForm 
from .models import Atividade
from django.forms import DateTimeField

class AtividadeForm(ModelForm):
    horario = DateTimeField()
    class Meta:
        model = Atividade
        fields = ['autor', 'titulo', 'descricao', 'tipo', 'horario', 'sala']
from django.db import models

class Atividade(models.Model):
    TIPO_ATIVIDADE = (
        ('PALESTRA', 'Palestra'), 
        ('MINICURSO', 'Minicurso')
    )
    autor = models.ForeignKey("Pessoa", on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    tipo = models.CharField(max_length=9, choices=TIPO_ATIVIDADE, default='MINICURSO')
    horario = models.DateTimeField()
    sala = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.autor}, {self.tipo}, {self.descricao} às {self.horario}.'

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
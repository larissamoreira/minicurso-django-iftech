from django.db import models

class Atividade(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    tipo = models.CharField(max_length=9)
    horario = models.DateTimeField()
    sala = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.autor}, {self.tipo}, {self.descricao} às {self.horario}.'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.programacao_list, name="programacao_list"),
    path('<int:atividade_id>/', views.programacao_detail, name="programacao_detail"),
    path('deletar/<int:atividade_id>/', views.programacao_delete, name="programacao_delete"),
    path('editar/<int:atividade_id>/', views.programacao_edit, name="programacao_edit"),
    path('create/', views.programacao_create, name="programacao_create")
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy


# Create your views here.


def home(request):
    # return HttpResponse('<h1>view Home</h1>')
    return render(request, "todos\home.html")


# def todoListar(request):
#     # tarefas = [{
#     #     'id':'1',
#     #     'Tarefa':'comprar fraldas'
#     # }]


#     tarefas = Todo.objects.all()  # busca todos os dados do banco


#     return render(request, "todos/todolistar.html",{'tarefas':tarefas})
class todoListarView(ListView):
    model = Todo #classe deve usar o modelo ToDo (.\todos\models.py) 

class todoCriarView(CreateView):
    model = Todo
    fields = ["nome","cpf","email","dtEntrada"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')
class todoAtualizarView(UpdateView):
    model = Todo
    fields = ["nome","cpf","email","dtEntrada"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Atualizar cadastro'
        return context
    
class todoDeletarView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_listar')
    template_name = "todos/todo_confirm_delete.html"
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,View
from .models import Todo
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,redirect
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoCreateView(LoginRequiredMixin,CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)

class TodoUpdateView(LoginRequiredMixin,UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

class TodoDeleteView(LoginRequiredMixin,DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoCompleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        todo = get_object_or_404(Todo,pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")

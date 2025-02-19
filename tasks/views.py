from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import TodoList
from django.urls import reverse_lazy

# Create your views here.
class TodoListListView(LoginRequiredMixin, ListView):

    login = reverse_lazy('account_login')
    template_name = 'tasks/index.html'

    def get_queryset(self):
        return TodoList.objects.for_user(self.request.user)

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cheats.models import Cheat, Category


class CheatListView(ListView):
    model = Cheat
    extra_context = {
        'title': 'Шпаргалки'
    }

    def get(self, request,  *args, **kwargs):
        category = request.GET.get('category', None)
        if category:
            self.queryset = self.get_queryset().filter(category=category)
        return super().get(request, args, kwargs)

    def get_context_data(self, **kwargs):
        title = self.queryset.select_related().first().category.title if self.queryset else None
        return super().get_context_data(category=title, **kwargs)


class CheatDetailView(DetailView):
    model = Cheat

    def get_context_data(self, **kwargs):
        return super().get_context_data(title=self.object.title, **kwargs)


class CheatCreateView(CreateView):
    model = Cheat
    fields = ('title', 'category', 'body', 'status')
    success_url = '/'
    extra_context = {
        'title': 'Добавить шпаргалку'
    }


class CheatUpdateView(UpdateView):
    model = Cheat
    fields = ('title', 'category', 'body', 'status')
    success_url = '/'
    extra_context = {
        'title': 'Редактировать шпаргалку'
    }


class CheatDeleteView(DeleteView):
    model = Cheat
    success_url = '/'

    def get_context_data(self, **kwargs):
        return super().get_context_data(title=f'Удалить {self.object.title}', **kwargs)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории'
    }


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        return super().get_context_data(title=self.object.title, **kwargs)


class CategoryCreateView(CreateView):
    model = Category
    fields = ('title', 'logo')
    success_url = '/'
    extra_context = {
        'title': 'Добавить категрию'
    }


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def get_context_data(self, **kwargs):
        return super().get_context_data(title=f'Удалить {self.object.title}', **kwargs)
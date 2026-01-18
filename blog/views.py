from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from  .models import Blogs


class BlogListView(ListView):
    model = Blogs
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication=True)


class BlogDetailView(DetailView):
    model = Blogs
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=['views'])  # Сохраняем только поле views_count

        return obj


class BlogCreateView(CreateView):
    model = Blogs
    fields = ['heading', 'content', 'preview']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blogs
    fields = ['heading', 'content', 'preview']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')


class MyModelDeletView(DeleteView):
    model = Blogs
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
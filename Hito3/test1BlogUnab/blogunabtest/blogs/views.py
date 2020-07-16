#from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#vista home
class HomePageView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
#vista blog
class HomeBlogsView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'blogs.html', {'blogs': Blog.blogs.all()})  

class DetallesBlogView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        id = kwargs["pk"]
        return render(request, 'blog.html', {'blog': Blog.blogs.get(id=id)})

class BlogCreate(CreateView):
    model = Blog
    template_name = './blog_form.html'
    fields = '__all__'

class BlogUpdate(UpdateView):
    model = Blog
    template_name = './blog_form.html'
    fields = ['titulo', 'contenido']

class BlogDelete(DeleteView):
    model = Blog
    template_name = './blog_confirm_delete.html'
    success_url = reverse_lazy('blogs')


   





#clave valor, clave blogs, luego a blogs.nombre, blogs.caca

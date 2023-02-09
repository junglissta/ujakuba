from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, View, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = 'login'

class HomeView(TemplateView):
    template_name = "index.html"
    model = Post
   
# class PostView(LoginRequiredMixin, ListView):
#     model = Post
#     template_name = 'posts.html'

class PostView(LoginRequiredMixin, FormView):
    form_class = PostForm
    template_name = 'posts.html'
    success_url = 'posts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('date')
        p = Paginator(context, 15)
        
        return context

    def post(self, request):
        posts = PostForm(request.POST)
        if posts.is_valid():
            posts.instance.user = request.user
            posts.save()
            return redirect('posts')
       
        return render(request, "posts.html", context={"posts": posts})

def signout(request):
    logout(request)
    return redirect('/')
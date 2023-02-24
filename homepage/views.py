from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator
from django.urls import reverse_lazy
# Create your views here.

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class HomeView(TemplateView):
    template_name = "index.html"
    model = Post
   
# class PostView(LoginRequiredMixin, ListView):
#     model = Post
#     template_name = 'posts.html'

class PostView(LoginRequiredMixin, ListView):
    model = Post
    form_class = PostForm
    template_name = 'posts.html'
    success_url = 'posts'
    queryset = Post.objects.all().order_by('-date')
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['form'] = PostForm
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
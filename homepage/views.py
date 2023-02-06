from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = 'login'

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
   
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings


# Create your views here.
def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject= form.cleaned_data["email"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            send_mail(subject, message, from_email, ["korcmaujakuba@gmail.com"])
            return redirect("success")
    return render(request, "contact/contact.html", {"form": form})

def successView(request):
    return render(request, 'contact/dakujeme.html')
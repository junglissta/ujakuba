from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


# Create your views here.
def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject='', message=message, from_email=from_email, recipient_list=["kubodemko@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contact\contact.html", {"form": form})

def successView(request):
    return HttpResponse("Mail Poslany")
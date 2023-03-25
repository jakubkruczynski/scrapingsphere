from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            try:
                sender_email = settings.EMAIL_HOST_USER
                recipient_list = ['contact@scrapingsphere.com']
                subject = f"New message from {name} - {email}"
                message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                send_mail(subject, message_body, sender_email, recipient_list)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "email.html", {"form": form})

def successView(request):
    return render(request, "success.html")

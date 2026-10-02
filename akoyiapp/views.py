from .models import viewers
from .models import consultants
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        client_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save message to database
        all = viewers(
            name=name,
            email=client_email,
            subject=subject,
            message=message,
        )

        all.save()

        # Email content
        email_message = f"""
New message from your portfolio website.

Name: {name}
Email: {client_email}

Subject:
{subject}

Message:
{message}
"""

        # Send email to you
        email = EmailMessage(
            subject=subject,
            body=email_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
            reply_to=[client_email],
        )

        email.send(fail_silently=False)

        return render(request, 'contact.html')

    return render(request, 'contact.html')

def portfoliodetails(request):
    return render(request, 'portfolio-details.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def resume(request):
    return render(request, 'resume.html')


def servicedetails(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        client_email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save consultation to database
        all = consultants(
            name=name,
            email=client_email,
            phone=phone,
            subject=subject,
            message=message,
        )

        all.save()

        # Create email
        email_message = f"""
New consultation request from your portfolio website.

Name: {name}
Email: {client_email}
Phone: {phone}

Message:
{message}
"""

        email = EmailMessage(
            subject=subject,
            body=email_message,
            from_email='akoyiwilliam79@gmail.com',
            to=['akoyiwilliam79@gmail.com'],
            reply_to=[client_email],
        )

        # Send email
        email.send(fail_silently=False)

        return render(request, 'service-details.html')

    return render(request, 'service-details.html')

def services(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        client_email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_message = f"""
New consultation request from your portfolio website.

Name: {name}
Email: {client_email}
Phone: {phone}

Message:
{message}
"""

        email = EmailMessage(
            subject=subject,
            body=email_message,
            from_email='akoyiwilliam79@gmail.com',
            to=['akoyiwilliam79@gmail.com'],
            reply_to=[client_email],
        )

        email.send(fail_silently=False)

        return render(request, 'services.html')

    return render(request, 'services.html')


def starterpage(request):
    return render(request, 'starter-page.html')
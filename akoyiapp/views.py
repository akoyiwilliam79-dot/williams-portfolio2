from django.shortcuts import render
from .models import viewers
from .models import consultants
# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
     
     if request.method == 'POST':
          all = viewers(
               name =request.POST['name'],
               email =request.POST['email'],
               subject =request.POST['subject'],
               message =request.POST['message'],
          )   
          all.save()
          return render(request,'contact.html')
     else:
          return render(request,'contact.html')


def portfoliodetails(request):
    return render(request,'portfolio-details.html')

def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')

def servicedetails(request):
    if request.method == 'POST':
          all = consultants(
               name =request.POST['name'],
               email =request.POST['email'],
               phone = request.POST['phone'],
               subject =request.POST['subject'],
               message =request.POST['message'],
          )   
          all.save()
          return render(request,'service-details.html')
    else:
          return render(request,'service-details.html')


def services(request):
    return render(request,'services.html')

def starterpage(request):
    return render(request,'starter-page.html')
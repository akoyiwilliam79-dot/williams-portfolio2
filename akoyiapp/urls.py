
from django.contrib import admin
from django.urls import path
from akoyiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

path('', views.home, name = 'home'),

path('about/', views.about, name = 'about'),

path('contact/', views.contact, name = 'contact'),

path('portfoliodetails/', views.portfoliodetails, name = 'portfolio-details'),

path('portfolio/', views.portfolio, name = 'portfolio'),

path('resume/', views.resume, name = 'resume'),

path('servicedetails/', views.servicedetails, name = 'service-details'),

path('services/', views.services, name = 'services'),

path('starterpage/', views.starterpage, name = 'starter-page'),




    
]

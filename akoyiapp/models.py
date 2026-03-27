from django.db import models

# Create your models here.

class viewers(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


   



class consultants(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=80)
    subject = models.TextField()
    message = models.TextField()


    def __str__(self):
        return self.name
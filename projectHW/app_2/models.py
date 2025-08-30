from django.db import models

# Create your models here.

class Company(models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class CEO(models.Model) :
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    biography = models.TextField('Write you mini-biography here, please!')

    def __str__(self):
        return self.name


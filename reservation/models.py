from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    phone = models.IntegerField(max_length=20)
    number = models.IntegerField(default=0)
    date = models.DateField(auto_now=False,auto_now_add=False)
    time = models.TimeField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.name

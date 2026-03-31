from django.db import models

# Create your models here.
class player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    date_joined = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    contact_person = models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.user.first_name


class Person(models.Model):
    name = models.CharField()
    birth = models.DateField()
    death = models.DateField()
    bio = models.TextField()

class Memory(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_('Person'))
    memory = models.TextField()
    
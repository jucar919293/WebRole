from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    """ Profile model
    Proxy model that extend the user model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    codeUTEC = models.CharField(max_length=10)
    nTokens = models.IntegerField(default=0)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    
    TYPE_MEMBER_CHOICES = [
        ('N','New'),
        ('C','Copper'),
        ('S','Silver'),
        ('G','Gold'),
    ]
    typeMember = models.CharField(max_length=50,
                                  choices=TYPE_MEMBER_CHOICES,
                                  default='N')
    
    CARRERA_CHOICES = [
        ('N','Null'),
        ('EL','Electrónica'),
        ('MT','Mecatrónica'),
        ('IN','Industrial'),
    ]
    carrera = models.CharField(max_length=50,
                               choices=CARRERA_CHOICES,
                               default='N')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """ Return username in admin"""
        return self.user.username


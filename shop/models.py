from django.db import models
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse


LABEL_CHOICES = (
    ('H', 'house'),
    ('C', 'comunication'),
    ('O', 'other')
)



class Item(models.Model):
    title = models.CharField(max_length=250)
    model = models.CharField(max_length=100, null=True)
    price = models.FloatField(max_length=100000, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, null=True)        
    frontcamera = models.CharField(max_length=100, null=True, blank=True)
    maincamera = models.CharField(max_length=150, null=True, blank=True)
    batary = models.IntegerField(null=True, blank=True)
    simcard = models.IntegerField(blank=True, null=True)
    memory = models.IntegerField(blank=True, null=True)
    shida = models.IntegerField(blank=True, null=True)
    screen = models.TextField(blank=True,null = True, max_length=120)
    systeminfo = models.TextField(blank=True, null= True, max_length=120)
    size = models.CharField(blank=True, null=True, max_length=90)
    date = models.DateField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(blank=True)
    supplies = models.IntegerField(null=True) 

    def __str__(self):
        return self.title

    def finalprice(self):
        finalpr = self.price - self.price * (self.discount_price/100)
        return finalpr
        
        

class ItemImage(models.Model):
    post = models.ForeignKey(Item, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'images/')
    

    def __str__(self):
        return self.post.title
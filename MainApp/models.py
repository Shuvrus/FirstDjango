from django.db import models


class Color(models.Model):
   name = models.CharField(max_length=32)

   def __str__(self):
      return f'{self.name}'


class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description = models.TextField(max_length=1000, default="Базовое описание")
   colors = models.ManyToManyField(to=Color)

   def __repr__(self):
       return F"Item: {self.name} | {self.brand}"




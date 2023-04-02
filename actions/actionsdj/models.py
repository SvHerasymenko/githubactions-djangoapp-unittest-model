from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField('Name', max_length = 100)
    description = models.TextField('Description', max_length = 250)
    price = models.FloatField('Price')
    url = models.CharField('Url',max_length = 100)
    status = models.BooleanField('Status')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural= "Products"

class User(models.Model):
    name = models.CharField('Name', max_length = 100)
    email = models.CharField('Email',max_length = 100)
    phone = models.IntegerField('Phone')
    balance = models.FloatField('Balance')
    status = models.BooleanField('Status')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural= "Users"

class Hero(models.Model):
    name = models.CharField('Name',max_length = 100)
    hitpoint = models.IntegerField('Hitpoint')
    power_attack = models.IntegerField('Power_attack')
    armor = models.FloatField('Armor')
    speed = models.FloatField('Speed')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural= "Heroes"
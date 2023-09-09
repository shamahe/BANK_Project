from django.db import models

from datetime import datetime,date


class District(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class AccountType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(blank=False,default=date.today())
    age = models.IntegerField(null=True, blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=300)
    email_id = models.EmailField(max_length=254)
    address = models.CharField(max_length=300)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True)




    def __str__(self):
        return self.name






















































































































































































































































































































    

    def __str__(self):
        return self.name





class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(blank=False,default=date.today())
    age = models.IntegerField(null=True, blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    phone_number = models.IntegerField(null=True, blank=False)
    email_id = models.EmailField(max_length=254)
    address = models.CharField(max_length=300)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True)




    def __str__(self):
        return self.name
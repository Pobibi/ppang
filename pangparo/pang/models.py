from django.db import models

# Create your models here.

class Pangstore(models.Model):
    stonum=models.IntegerField(primary_key=True)
    pw=models.CharField(max_length=20)
    stoname=models.CharField(max_length=30)
    stoadd=models.CharField(max_length=50)
    objects=models.Manager()




class Panglist(models.Model):
    pangnum=models.IntegerField(primary_key=True,unique=True,auto_created=True)
    stonum=models.ForeignKey('Pangstore',on_delete=models.CASCADE)
    pangname=models.CharField(max_length=30)
    pangcate=models.CharField(max_length=20)
    pangimg=models.ImageField(upload_to='media',blank=True)
    pangcount=models.IntegerField()
    panginfo=models.CharField(max_length=1000)
    pangal=models.CharField(max_length=1000)
    objects=models.Manager()
   


class Panguser(models.Model):
    usernum=models.IntegerField(primary_key=True,unique=True)
    pw=models.CharField(max_length=20)
    like=models.ForeignKey('Panglist',on_delete=models.CASCADE)
    objects=models.Manager()
   




from django.db import models

# Create your models here.
class Hoodies(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Joggers(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Facemasks(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Cosplay(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Backpacks(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Rings(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Animelist(models.Model):
    rank = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    rating = models.FloatField()
    image_url = models.CharField(max_length=2083)
    video_url = models.CharField(max_length=100)



class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=50
    )
    logo = models.FileField(
        upload_to='logo/'
    )
    bishkek_number = models.CharField(
        max_length=55
    )
    osh_number = models.CharField(
        max_length=55
    )
    ja_number = models.CharField(
        max_length=55
    )
    ik_number = models.CharField(
        max_length=55
    )
    students = models.CharField(
        max_length=25
    )
    exp = models.CharField(
        max_length=25
    )
class Review(models.Model):
    full_name = models.CharField(
        max_length=55
    )
    work = models.CharField(
        max_length=55
    )
    text = models.TextField(
        max_length=1000
    )
    image = models.ImageField(
        upload_to='review_image/'
    )
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    
class Otklic(models.Model):
    full_name = models.CharField(
        max_length= 55
    )
    phone_number = models.CharField(
        max_length=22
    )
    sity = models.CharField(
        max_length=255
    )
    message = models.TextField(
        max_length=500
    )
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        

class Gallery(models.Model):
    image = models.FileField(
        verbose_name='Фотография галлереи',
        upload_to='gallery/',
    )

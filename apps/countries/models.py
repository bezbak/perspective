from django.db import models

# Create your models here.
class Countries(models.Model):
    title = models.CharField(
        max_length=255
    )
    author = models.CharField(
        max_length=100
    )
    date = models.DateField(
        auto_now_add=False
    )
    image = models.FileField(
        upload_to='countries/'
    )
    description = models.TextField(
        max_length=1000
    )
    quote = models.CharField(
        max_length=255
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        

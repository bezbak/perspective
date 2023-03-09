from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(
        max_length= 55
    )
    experience = models.CharField(
        max_length=55
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
    
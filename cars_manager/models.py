from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.urls import reverse


class Brand(models.Model):
    '''
    Производитель
    '''

    name = models.CharField(max_length=128, null=False, blank=False, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

class Car(models.Model):
    '''
    Автомобиль
    '''

    make = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Марка")
    model = models.CharField(max_length=256, null=False, blank=False, verbose_name="Модель")
    year = models.PositiveIntegerField(validators=[MaxValueValidator(3000)],null=False, blank=False, verbose_name="Год")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="D&T создания")
    uploaded_at = models.DateTimeField(auto_now=True, verbose_name="D&T обновления")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Владелец")

    def __str__(self):
        return " ".join([str(self.make), self.model, str(self.year)])
    
    def get_absolute_url(self):
        return reverse('car_details', kwargs={'car_id': self.id})

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

class Comments(models.Model):
    '''
    Комментарий
    '''

    content = models.TextField(max_length=4096, verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="D&T создания")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль", related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Автор")
    # Внешний ключ для создания ответов на комментарии
    parent = models.ForeignKey('self' , null=True , blank=True, on_delete=models.CASCADE , related_name='replies')

    def __str__(self):
        return f"{self.created_at.date()} {self.created_at.time()}, {self.author.first_name} {self.author.last_name}"

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
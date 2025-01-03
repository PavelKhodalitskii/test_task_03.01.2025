from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    '''
    Производитель
    '''
    name = models.CharField(max_length=128, null=False, blank=False, verbose_name="Название")

    class Meta:
        pass

class Car(models.Model):
    '''
    Автомобиль
    '''

    make = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Марка")
    model = models.CharField(max_length=256, null=False, blank=False, verbose_name="Модель")
    year = models.IntegerField(null=False, blank=False, verbose_name="Год")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="D&T создания")
    uploaded_at = models.DateTimeField(auto_now=True, verbose_name="D&T обновления")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Владелец")

    class Meta:
        pass

class Comments(models.Model):
    '''
    Комментарий
    '''

    content = models.TextField(max_length=4096, verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="D&T создания")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="Автор")
    # Внешний ключ для создания ответов на комментарии
    parent = models.ForeignKey('self' , null=True , blank=True, on_delete=models.CASCADE , related_name='replies')
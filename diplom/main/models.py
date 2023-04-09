from django.db import models
from django import forms


class CorouselCommon(models.Model):
    title = models.CharField(verbose_name='Название', max_length=25, default="")
    description = models.CharField(verbose_name='Описание', max_length=150, default="")
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Изображение', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class CoroselProducts(CorouselCommon):
    price = models.CharField(verbose_name='Цена', max_length=20, default="")
    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"

class CoroselReviews(CorouselCommon):
    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"

from django.db import models


class Assort(models.Model):
    title = models.CharField('название', max_length=15, default="")
    opisanie = models.CharField('название', max_length=40, default="")
    image_tov = models.ImageField()


class otz(models.Model):
    title = models.CharField('название', max_length=15, default="")
    opisanie = models.CharField('название', max_length=45, default="")
    image_tov = models.ImageField()


def __str__(self):
    return self.title



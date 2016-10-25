from django.db import models


class List(models.Model):
    list = models.IntegerField(default=0)


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

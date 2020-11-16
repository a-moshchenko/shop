from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='категория')


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='подкатегория')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name='категория')


class Clothes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name='категория')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT,
                                    verbose_name='подкатегория')

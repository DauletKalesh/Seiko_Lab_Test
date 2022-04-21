from django.db import models


# Create your models here.
class Shops(models.Model):
    shop_name = models.CharField(verbose_name='Магазины', max_length=255, null=False)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
    
    def __str__(self) -> str:
        return self.shop_name

class Categories(models.Model):
    category_name = models.CharField(verbose_name='Категории', max_length=255, null=False)
    shop_id = models.ManyToManyField('Shops')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self) -> str:
        return self.category_name

class Items(models.Model):
    item_name = models.CharField(verbose_name='Товары', max_length=255, null=False)
    category_id = models.ForeignKey('Categories', on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.item_name
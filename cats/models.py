from django.db import models

from users.models import NULLABLE

class Bread(models.Model):
    name = models.CharField(max_length=100, verbose_name='bread')
    description = models.CharField(max_length=1000, verbose_name='description', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'bread'
        verbose_name_plural = 'breads'


class Cats(models.Model):
    name = models.CharField(max_length=250, verbose_name='cat name')
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE, verbose_name='bread')
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='image')
    birth_date = models.DateField(**NULLABLE,verbose_name='birth_date')

    def __str__(self):
        return f'{self.name} ({self.bread})'

    class Meta:
        verbose_name = 'cat'
        verbose_name_plural = 'cats'
        # abstract = True
        # app_label = 'cats'
        # ordering = [-1]
        # permissions = []
        # db_table = 'cat_table'
        # get_latest_by = 'birth_date'
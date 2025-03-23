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

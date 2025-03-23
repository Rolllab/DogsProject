# Generated by Django 5.1.7 on 2025-03-23 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='dog name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dogs/', verbose_name='image')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth_date')),
                ('bread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.bread', verbose_name='bread')),
            ],
            options={
                'verbose_name': 'dog',
                'verbose_name_plural': 'dogs',
            },
        ),
    ]

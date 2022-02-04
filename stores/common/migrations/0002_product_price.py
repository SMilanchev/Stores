# Generated by Django 3.2.11 on 2022-02-02 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=2, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]

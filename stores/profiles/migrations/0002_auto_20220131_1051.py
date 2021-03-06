# Generated by Django 3.2.11 on 2022-01-31 08:51

from django.db import migrations, models
import stores.store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, validators=[stores.store.validators.capital_first_letter]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, validators=[stores.store.validators.capital_first_letter]),
        ),
    ]

# Generated by Django 3.2.11 on 2022-01-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20220131_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
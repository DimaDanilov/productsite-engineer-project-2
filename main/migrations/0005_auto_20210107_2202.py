# Generated by Django 3.1.5 on 2021-01-07 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210107_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salerman',
            name='salername',
            field=models.CharField(max_length=25, verbose_name='ФИО'),
        ),
    ]

# Generated by Django 2.0.3 on 2018-03-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strelka', '0004_auto_20180325_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='money',
            field=models.FloatField(verbose_name='Кол-во денег на счету'),
        ),
    ]

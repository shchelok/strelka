# Generated by Django 2.0.3 on 2018-04-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strelka', '0012_auto_20180330_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='number_card',
            field=models.CharField(max_length=11, verbose_name='Номер карты'),
        ),
    ]
# Generated by Django 2.0.3 on 2018-04-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strelka', '0013_auto_20180401_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='balance',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Баланс карты'),
        ),
    ]
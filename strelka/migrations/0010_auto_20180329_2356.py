# Generated by Django 2.0.3 on 2018-03-29 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strelka', '0009_auto_20180329_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='money',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moneys', to='strelka.Money'),
        ),
    ]

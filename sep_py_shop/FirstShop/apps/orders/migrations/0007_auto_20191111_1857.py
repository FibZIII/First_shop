# Generated by Django 2.2.4 on 2019-11-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191109_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('CA', 'Cash'), ('CR', 'Credit'), ('PP', 'PrivatPay'), ('POP', 'Pay of parts'), ('POC', 'Pay of card')], max_length=100, null=True),
        ),
    ]

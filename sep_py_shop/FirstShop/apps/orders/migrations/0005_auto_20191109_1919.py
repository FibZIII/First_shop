# Generated by Django 2.2.4 on 2019-11-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191109_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Credit', 'Credit'), ('PrivarPay', 'PrivarPay'), ('Pay_of_parts', 'Pay of parts'), ('Pay_of_card', 'Pay of card')], max_length=100, null=True),
        ),
    ]

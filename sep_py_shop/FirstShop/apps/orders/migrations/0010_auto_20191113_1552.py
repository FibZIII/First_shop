# Generated by Django 2.2.4 on 2019-11-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20191113_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(default='CR', max_length=100, null=True),
        ),
    ]

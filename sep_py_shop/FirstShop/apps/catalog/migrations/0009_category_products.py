# Generated by Django 2.2.4 on 2019-12-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('catalog', '0008_merge_20191119_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]

# Generated by Django 2.2.4 on 2019-12-01 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0025_orderitem_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product_id',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_product', to='products.Product'),
        ),
    ]

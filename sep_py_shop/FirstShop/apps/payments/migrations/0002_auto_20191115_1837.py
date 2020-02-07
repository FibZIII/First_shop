# Generated by Django 2.2.4 on 2019-11-15 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='reason',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
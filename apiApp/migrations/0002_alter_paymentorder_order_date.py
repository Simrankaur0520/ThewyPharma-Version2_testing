# Generated by Django 4.0.3 on 2023-12-14 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentorder',
            name='order_date',
            field=models.TextField(default='2023-12-14 22:55:06.445843+05:30'),
        ),
    ]
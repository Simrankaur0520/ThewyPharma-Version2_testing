# Generated by Django 4.0.3 on 2023-12-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiApp', '0002_remove_user_data_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentorder',
            name='order_date',
            field=models.TextField(default='2023-12-14 22:40:19.964525+05:30'),
        ),
    ]

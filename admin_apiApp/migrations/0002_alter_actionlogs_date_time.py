# Generated by Django 4.0.3 on 2023-12-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_apiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionlogs',
            name='date_time',
            field=models.TextField(default='2023-12-14 22:54:11.908837+05:30'),
        ),
    ]

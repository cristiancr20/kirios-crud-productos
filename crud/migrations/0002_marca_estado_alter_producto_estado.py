# Generated by Django 5.0.6 on 2024-05-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='estado',
            field=models.CharField(default='True', max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.CharField(default='True', max_length=50),
        ),
    ]

# Generated by Django 3.1.2 on 2025-01-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_lockedproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lockedproduct',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2025-01-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0009_auto_20250101_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='batch_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
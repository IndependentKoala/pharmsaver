# Generated by Django 3.1.2 on 2024-12-01 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='customer',
            new_name='client',
        ),
    ]
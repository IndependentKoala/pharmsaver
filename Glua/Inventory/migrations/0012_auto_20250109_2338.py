# Generated by Django 3.1.2 on 2025-01-09 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0011_remove_sale_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lockedproduct',
            name='drug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Inventory.drug'),
        ),
    ]

# Generated by Django 4.2.17 on 2025-02-16 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0018_alter_drug_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('client', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('batch_no', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('in_stock', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.drug')),
            ],
        ),
    ]

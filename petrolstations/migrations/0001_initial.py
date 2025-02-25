# Generated by Django 5.1.6 on 2025-02-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetrolStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('diesel_price', models.DecimalField(blank=True, decimal_places=3, max_digits=5)),
                ('e5_price', models.DecimalField(blank=True, decimal_places=3, max_digits=5)),
                ('e10_price', models.DecimalField(blank=True, decimal_places=3, max_digits=5)),
                ('electric_fueling', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_product_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedproduct',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-29 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_product_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('brand', 'name')},
        ),
    ]

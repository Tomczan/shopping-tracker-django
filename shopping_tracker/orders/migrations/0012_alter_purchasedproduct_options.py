# Generated by Django 4.1.3 on 2023-04-13 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_purchasedproduct_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchasedproduct',
            options={'ordering': ['-updated', 'product']},
        ),
    ]

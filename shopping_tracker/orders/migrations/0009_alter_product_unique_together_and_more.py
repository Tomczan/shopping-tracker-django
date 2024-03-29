# Generated by Django 4.1.3 on 2022-11-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_product_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('brand', 'name'), name='unique_product_with_a_particular_brand'),
        ),
    ]

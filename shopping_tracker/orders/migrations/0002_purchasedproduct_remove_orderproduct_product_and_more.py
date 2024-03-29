# Generated by Django 4.1.3 on 2022-11-24 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('opened', models.DateField(blank=True, null=True)),
                ('finished', models.DateField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.shop')),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]

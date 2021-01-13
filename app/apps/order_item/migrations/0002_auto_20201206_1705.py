# Generated by Django 3.1.3 on 2020-12-06 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('order', '0002_auto_20201206_1659'),
        ('order_item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    related_name='order_item', to='order.order',
                                    verbose_name='Sipariş'),
        ),
    ]

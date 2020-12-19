# Generated by Django 3.1.3 on 2020-12-06 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201206_1659'),
        ('order_item', '0002_auto_20201206_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderitem', to='order.order', verbose_name='Sipariş'),
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('order_item', '0003_auto_20201206_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total_amount',
            field=models.FloatField(default=0, verbose_name='Toplam Tutar'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total_amount_with_vat',
            field=models.FloatField(default=0,
                                    verbose_name='Toplam Tutar (KDVli)'),
        ),
    ]

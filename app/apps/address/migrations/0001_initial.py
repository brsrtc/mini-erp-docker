# Generated by Django 3.1.3 on 2020-12-05 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import core.cache


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True,
                                                    verbose_name='Updated At')),
                ('is_active',
                 models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted',
                 models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True,
                                                    verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('slot', models.IntegerField(default=1, verbose_name='Slot')),
                ('use_in',
                 models.BooleanField(default=False, verbose_name='Use In')),
            ],
            options={
                'ordering': ['slot', 'name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.CreateModel(
            name='Township',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True,
                                                    verbose_name='Updated At')),
                ('is_active',
                 models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted',
                 models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True,
                                                    verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('city',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                   to='address.city', verbose_name='City')),
                ('created_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_township_created_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_township_deleted_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_township_updated_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Updated By')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True,
                                                    verbose_name='Updated At')),
                ('is_active',
                 models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted',
                 models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True,
                                                    verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('code', models.CharField(max_length=16, verbose_name='Code')),
                ('created_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_state_created_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_state_deleted_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_state_updated_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Updated By')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True,
                                                    verbose_name='Updated At')),
                ('is_active',
                 models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted',
                 models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True,
                                                    verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('created_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_district_created_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_district_deleted_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Deleted By')),
                ('township',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                   to='address.township',
                                   verbose_name='Township')),
                ('updated_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_district_updated_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Updated By')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True,
                                                    verbose_name='Updated At')),
                ('is_active',
                 models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted',
                 models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True,
                                                    verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('code', models.CharField(max_length=16, verbose_name='Code')),
                ('slot', models.IntegerField(default=1, verbose_name='Slot')),
                ('default_country', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_country_created_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_country_deleted_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Deleted By')),
                ('updated_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_country_updated_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Updated By')),
            ],
            options={
                'ordering': ['slot', 'name'],
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    to='address.country',
                                    verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.PROTECT,
                                    related_name='address_city_created_by',
                                    to=settings.AUTH_USER_MODEL,
                                    verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='city',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.PROTECT,
                                    related_name='address_city_deleted_by',
                                    to=settings.AUTH_USER_MODEL,
                                    verbose_name='Deleted By'),
        ),
        migrations.AddField(
            model_name='city',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.PROTECT,
                                    related_name='address_city_updated_by',
                                    to=settings.AUTH_USER_MODEL,
                                    verbose_name='Updated By'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True,
                                                    verbose_name='Updated At')),
                ('is_active',
                 models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_deleted',
                 models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('deleted_at', models.DateTimeField(blank=True, null=True,
                                                    verbose_name='Deleted At')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('address_title', models.CharField(max_length=512,
                                                   verbose_name='Address Title')),
                ('address', models.TextField()),
                ('postal_code',
                 models.CharField(blank=True, max_length=10, null=True,
                                  verbose_name='Postal Code')),
                ('phone',
                 models.CharField(help_text='Örn: 5301234567', max_length=32,
                                  verbose_name='Phone')),
                ('internal',
                 models.CharField(blank=True, max_length=64, null=True,
                                  verbose_name='Dahili')),
                ('fax',
                 models.CharField(blank=True, help_text='Örn: 2122454545',
                                  max_length=64, null=True,
                                  verbose_name='Fax')),
                ('name', models.CharField(blank=True, max_length=256, null=True,
                                          verbose_name='Name')),
                ('identity_number',
                 models.CharField(blank=True, max_length=64, null=True,
                                  verbose_name='Identity Number')),
                ('tax_no',
                 models.CharField(blank=True, max_length=256, null=True,
                                  verbose_name='Tax No')),
                ('tax_office',
                 models.CharField(blank=True, max_length=256, null=True,
                                  verbose_name='Tax Office')),
                ('is_cancelled', models.BooleanField(default=False,
                                                     verbose_name='Is Cancelled')),
                ('cancelled_at', models.DateTimeField(blank=True, null=True,
                                                      verbose_name='Cancelled At')),
                ('city',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                   to='address.city', verbose_name='City')),
                ('created_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_address_created_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Created By')),
                ('deleted_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_address_deleted_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Deleted By')),
                ('district', models.ForeignKey(blank=True, null=True,
                                               on_delete=django.db.models.deletion.PROTECT,
                                               to='address.district',
                                               verbose_name='District')),
                ('state', models.ForeignKey(blank=True, null=True,
                                            on_delete=django.db.models.deletion.PROTECT,
                                            to='address.state',
                                            verbose_name='State')),
                ('township',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                   to='address.township',
                                   verbose_name='Township')),
                ('updated_by', models.ForeignKey(blank=True, null=True,
                                                 on_delete=django.db.models.deletion.PROTECT,
                                                 related_name='address_address_updated_by',
                                                 to=settings.AUTH_USER_MODEL,
                                                 verbose_name='Updated By')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
            bases=(models.Model, core.cache.BaseCache),
        ),
    ]

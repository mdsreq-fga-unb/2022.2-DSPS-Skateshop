# Generated by Django 3.2.4 on 2023-02-09 07:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20230209_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='limitedtimeoffer',
            name='absolute_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='limitedtimeoffer',
            name='relative_discount',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(95)]),
        ),
    ]

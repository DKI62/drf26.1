# Generated by Django 5.1.5 on 2025-01-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='product_price',
            field=models.PositiveIntegerField(verbose_name='Цена продукта'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='stripe_session_url',
            field=models.URLField(blank=True, max_length=2048, null=True, verbose_name='URL оплаты в Stripe'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-21 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_products', '0003_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]

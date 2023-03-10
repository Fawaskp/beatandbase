# Generated by Django 4.1.7 on 2023-02-21 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_category', '0001_initial'),
        ('admin_brand', '0001_initial'),
        ('admin_products', '0004_product_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_brand.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_category.categories'),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]

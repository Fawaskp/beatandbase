# Generated by Django 4.1.7 on 2023-03-02 01:18

from django.db import migrations, models
import user_home.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_home', '0012_delete_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='identification',
            field=models.IntegerField(default=user_home.models.generate_product_id, unique=True),
        ),
    ]
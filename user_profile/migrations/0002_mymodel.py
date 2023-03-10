# Generated by Django 4.1.7 on 2023-03-01 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(editable=False, unique=True)),
                ('modelname', models.CharField(max_length=100)),
                ('model_desc', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
    ]

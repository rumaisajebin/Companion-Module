# Generated by Django 5.0.6 on 2024-06-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companion_profile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

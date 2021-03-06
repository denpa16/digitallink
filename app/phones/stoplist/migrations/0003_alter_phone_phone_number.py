# Generated by Django 3.2.7 on 2021-10-26 11:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoplist', '0002_rename_phonemodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]

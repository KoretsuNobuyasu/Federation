# Generated by Django 2.1.5 on 2019-02-05 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesinformation', '0002_auto_20190205_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesinformation',
            name='result',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='大会結果'),
        ),
    ]

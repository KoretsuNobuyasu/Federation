# Generated by Django 2.1.5 on 2019-02-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesinformation', '0003_auto_20190205_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesinformation',
            name='guidelines',
            field=models.FileField(blank=True, upload_to='', verbose_name='大会要項'),
        ),
        migrations.AlterField(
            model_name='gamesinformation',
            name='result',
            field=models.FileField(blank=True, upload_to='', verbose_name='結果'),
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesinformation', '0004_auto_20190205_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesinformation',
            name='place',
            field=models.CharField(blank=True, max_length=50, verbose_name='開催地'),
        ),
    ]

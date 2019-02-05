# Generated by Django 2.1.5 on 2019-02-05 08:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリ名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='Gamesinformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='大会名')),
                ('text', models.TextField(verbose_name='本文')),
                ('guidelines', models.FileField(blank=True, upload_to='uploads/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['pdf, '])], verbose_name='大会要項')),
                ('result', models.FileField(blank=True, upload_to='uploads/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['pdf, '])], verbose_name='大会結果')),
                ('created_at', models.DateTimeField(verbose_name='開催日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gamesinformation.Category', verbose_name='カテゴリ')),
            ],
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0002_auto_20190201_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='top_page')),
            ],
        ),
    ]
# Generated by Django 3.2.10 on 2021-12-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0006_auto_20211226_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagebannerads',
            name='image',
            field=models.ImageField(upload_to='advertisement'),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='trendingnews',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]

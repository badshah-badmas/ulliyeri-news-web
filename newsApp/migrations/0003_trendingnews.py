# Generated by Django 3.2.10 on 2021-12-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_auto_20211226_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('news', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
# Generated by Django 3.2.10 on 2021-12-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0010_auto_20211227_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakingnews',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='entertainmentnews',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='homepagebannerads',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='latestnews',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trendingnews',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

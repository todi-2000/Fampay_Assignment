# Generated by Django 4.0.7 on 2022-08-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='published_date_time',
            field=models.DateTimeField(),
        ),
    ]
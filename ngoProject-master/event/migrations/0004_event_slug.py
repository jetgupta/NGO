# Generated by Django 2.2.2 on 2019-06-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20190618_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=0, max_length=200),
        ),
    ]
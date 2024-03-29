# Generated by Django 2.2.2 on 2019-06-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20190617_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='img/no_image.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(blank=True),
        ),
    ]

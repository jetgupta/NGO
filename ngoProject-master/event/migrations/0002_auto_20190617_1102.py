# Generated by Django 2.2.2 on 2019-06-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('c', 'Conference'), ('s', 'Seminar'), ('p', 'Presentation')], default='c', max_length=1),
        ),
    ]

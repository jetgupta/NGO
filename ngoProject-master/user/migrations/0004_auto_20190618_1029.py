# Generated by Django 2.2.2 on 2019-06-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190618_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('a', 'Admin'), ('u', 'User')], default='u', max_length=5),
        ),
    ]
# Generated by Django 2.2.2 on 2019-06-18 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='register',
            new_name='register_allowed',
        ),
    ]

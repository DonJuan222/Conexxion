# Generated by Django 4.1.3 on 2022-11-18 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_event_end_time_event_start_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='nombre',
            new_name='tipo',
        ),
    ]

# Generated by Django 2.2.6 on 2020-11-23 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='subject',
            new_name='slug',
        ),
    ]
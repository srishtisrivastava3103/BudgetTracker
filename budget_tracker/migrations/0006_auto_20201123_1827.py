# Generated by Django 2.2.6 on 2020-11-23 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_tracker', '0005_assets_liability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='description',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='liability',
            old_name='description',
            new_name='type',
        ),
    ]

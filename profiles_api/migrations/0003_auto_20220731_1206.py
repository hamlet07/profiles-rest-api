# Generated by Django 2.2 on 2022-07-31 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20220731_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='created_on_field',
            new_name='created_on',
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-29 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210728_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeruser',
            old_name='school',
            new_name='program',
        ),
    ]

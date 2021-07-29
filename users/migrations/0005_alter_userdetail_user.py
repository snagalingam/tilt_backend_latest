# Generated by Django 3.2.5 on 2021-07-29 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210729_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to=settings.AUTH_USER_MODEL),
        ),
    ]

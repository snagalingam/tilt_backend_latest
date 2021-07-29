# Generated by Django 3.2.5 on 2021-07-29 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_school_customeruser_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(choices=[('northwestern', 'northwestern')], max_length=100)),
                ('unique_id', models.CharField(blank=True, max_length=255)),
                ('preferred_name', models.CharField(blank=True, max_length=255)),
                ('program', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user detail',
                'verbose_name_plural': 'user details',
            },
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='user',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='CustomerUser',
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformuser',
            name='is_disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='platformuser',
            name='is_user_blocked',
            field=models.BooleanField(default=False),
        ),
    ]

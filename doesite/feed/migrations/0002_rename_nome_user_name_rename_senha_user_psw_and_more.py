# Generated by Django 4.2.1 on 2023-05-29 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='senha',
            new_name='psw',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tipo',
            new_name='type',
        ),
    ]

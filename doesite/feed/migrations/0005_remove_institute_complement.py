# Generated by Django 4.2.1 on 2023-05-30 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_alter_institute_email_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute',
            name='complement',
        ),
    ]

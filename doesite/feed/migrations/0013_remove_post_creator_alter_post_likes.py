# Generated by Django 4.2.1 on 2023-07-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_merge_20230715_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='creator',
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 4.2.1 on 2023-07-14 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.CharField(default='vazio', max_length=50),
        ),
    ]

# Generated by Django 4.2.1 on 2023-07-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0010_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creator',
            field=models.CharField(default='', max_length=50),
        ),
    ]

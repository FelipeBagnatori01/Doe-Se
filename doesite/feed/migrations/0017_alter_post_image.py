# Generated by Django 4.2.1 on 2023-07-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0016_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
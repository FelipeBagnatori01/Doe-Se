# Generated by Django 4.2.1 on 2023-07-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

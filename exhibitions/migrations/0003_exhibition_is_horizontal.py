# Generated by Django 2.2.1 on 2019-06-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitions', '0002_remove_exhibition_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='is_horizontal',
            field=models.BooleanField(default=True),
        ),
    ]
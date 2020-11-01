# Generated by Django 2.2.1 on 2020-05-14 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True)),
                ('is_published', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
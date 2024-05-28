# Generated by Django 5.0.6 on 2024-05-25 03:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogdata',
            fields=[
                ('Blog_Id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('User_Name', models.CharField(max_length=3)),
                ('Blog_Name', models.CharField(max_length=30)),
                ('Blog', models.TextField()),
            ],
        ),
    ]

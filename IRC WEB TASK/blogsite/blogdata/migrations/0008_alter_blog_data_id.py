# Generated by Django 5.0.6 on 2024-05-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogdata', '0007_blog_data_favourite_blog_data_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_data',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

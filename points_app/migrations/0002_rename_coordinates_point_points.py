# Generated by Django 3.2.19 on 2023-05-17 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='coordinates',
            new_name='points',
        ),
    ]

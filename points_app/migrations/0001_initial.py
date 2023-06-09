# Generated by Django 3.2.19 on 2023-05-17 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ClosestPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closest_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='closest_point', to='points_app.point')),
                ('original_points', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_points', to='points_app.point')),
            ],
        ),
    ]

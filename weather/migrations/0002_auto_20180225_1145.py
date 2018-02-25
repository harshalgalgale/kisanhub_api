# Generated by Django 2.0.2 on 2018-02-25 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weathermetricreading',
            name='location',
        ),
        migrations.RemoveField(
            model_name='weathermetricreading',
            name='metric',
        ),
        migrations.AddField(
            model_name='weathermetricreading',
            name='source',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='weather.DataSource'),
            preserve_default=False,
        ),
    ]
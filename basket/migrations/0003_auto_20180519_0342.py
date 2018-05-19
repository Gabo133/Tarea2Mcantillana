# Generated by Django 2.0.4 on 2018-05-19 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_auto_20180424_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='birthday',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='basket.Team'),
        ),
    ]
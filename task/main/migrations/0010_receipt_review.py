# Generated by Django 2.1.3 on 2018-11-25 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20181125_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Reviews'),
        ),
    ]

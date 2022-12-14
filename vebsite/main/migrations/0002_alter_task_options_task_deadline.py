# Generated by Django 4.0.6 on 2022-08-01 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, verbose_name='Срок исполнения'),
            preserve_default=False,
        ),
    ]

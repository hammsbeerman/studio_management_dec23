# Generated by Django 3.2.21 on 2023-09-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krueger', '0003_auto_20230922_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paperstock',
            name='paper',
        ),
        migrations.AddField(
            model_name='paperstock',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='brand'),
        ),
        migrations.AddField(
            model_name='paperstock',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='manufacturer'),
        ),
        migrations.AddField(
            model_name='paperstock',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='size'),
        ),
        migrations.AddField(
            model_name='paperstock',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='weight'),
        ),
    ]

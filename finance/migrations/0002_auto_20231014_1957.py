# Generated by Django 3.2.21 on 2023-10-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountspayable',
            name='amount_paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount Paid'),
        ),
        migrations.AlterField(
            model_name='accountspayable',
            name='date_paid',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accountspayable',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='accountspayable',
            name='discount_date_due',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accountspayable',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Invoice Number'),
        ),
    ]

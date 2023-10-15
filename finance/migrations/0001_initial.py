# Generated by Django 3.2.21 on 2023-10-15 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountsPayable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_recieved', models.DateField()),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('invoice_number', models.CharField(max_length=100, verbose_name='Invoice Number')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Amount')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Discount')),
                ('discount_date_due', models.DateField()),
                ('paid', models.BooleanField(null=True, verbose_name='Paid')),
                ('date_paid', models.DateField()),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.vendor')),
            ],
        ),
    ]
# Generated by Django 3.1.3 on 2020-11-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermodel',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment about the order'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='customer_email_address',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='customer_first_name',
            field=models.CharField(max_length=30, verbose_name="Customer's first name"),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='customer_last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Customer's last name"),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='customer_phone',
            field=models.CharField(max_length=20, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'New'), (1, 'In progress'), (2, 'Done')], default=0, verbose_name='Status'),
        ),
    ]

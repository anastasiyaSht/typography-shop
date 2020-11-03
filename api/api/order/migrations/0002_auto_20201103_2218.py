# Generated by Django 3.1.3 on 2020-11-03 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermodel',
            options={'verbose_name': 'Order'},
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='customer_email_address',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='customer_first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Open'), (2, 'In progress'), (3, 'Done')], null=True),
        ),
    ]
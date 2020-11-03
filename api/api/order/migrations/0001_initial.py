# Generated by Django 3.1.3 on 2020-11-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_first_name', models.CharField(max_length=50)),
                ('customer_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_phone', models.CharField(max_length=20)),
                ('customer_email_address', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.TextField()),
                ('status', models.SmallIntegerField(choices=[('OPEN', 1), ('IN PROGRESS', 2), ('DONE', 3)], null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
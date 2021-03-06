# Generated by Django 2.1 on 2018-09-13 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^(?:(55\\d{2})|\\d{2})[6-9]\\d{8}$')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['cpf'], name='cpf_index'),
        ),
    ]

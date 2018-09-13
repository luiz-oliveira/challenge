# Generated by Django 2.1 on 2018-09-13 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_debt', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debts', to='customers.Customer')),
            ],
        ),
    ]

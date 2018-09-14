# Generated by Django 2.1 on 2018-09-14 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_debt', models.DateField()),
                ('payment_type', models.CharField(max_length=100)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='customers.Customer')),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2025-04-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0033_expensecategory_expense_budget_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2025-04-07 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0022_alter_expense_patment_method_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='desription',
            new_name='description',
        ),
    ]

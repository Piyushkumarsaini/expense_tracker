# Generated by Django 5.1.2 on 2025-04-07 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0018_expense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='patment_method_id',
        ),
        migrations.DeleteModel(
            name='PatmentMethod',
        ),
    ]

# Generated by Django 5.1.2 on 2025-04-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0013_rename_name_category_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]

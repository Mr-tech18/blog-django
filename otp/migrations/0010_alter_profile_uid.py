# Generated by Django 5.0.6 on 2025-01-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0009_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='pr7f242f22', max_length=200),
        ),
    ]
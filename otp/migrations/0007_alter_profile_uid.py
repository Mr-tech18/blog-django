# Generated by Django 5.0.6 on 2025-01-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0006_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='pr5ce330b0', max_length=200),
        ),
    ]
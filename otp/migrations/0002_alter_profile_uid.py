# Generated by Django 5.0.6 on 2024-12-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x00000230F40F7560>', max_length=200),
        ),
    ]
# Generated by Django 5.0.6 on 2024-10-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_author_description_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

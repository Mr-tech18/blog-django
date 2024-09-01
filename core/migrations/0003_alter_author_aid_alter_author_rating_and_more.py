# Generated by Django 5.0.6 on 2024-09-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_author_aid_alter_category_cid_alter_post_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='aid',
            field=models.UUIDField(default='aut7bd4b10', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.CharField(blank=True, choices=[(1, '🌟⭐⭐⭐⭐'), (2, '🌟🌟⭐⭐⭐'), (3, '🌟🌟🌟⭐⭐'), (4, '🌟🌟🌟🌟⭐'), (5, '🌟🌟🌟🌟🌟')], default=1, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='cid',
            field=models.UUIDField(default='catdba7b6a', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Rating',
            field=models.IntegerField(blank=True, choices=[(1, '🌟⭐⭐⭐⭐'), (2, '🌟🌟⭐⭐⭐'), (3, '🌟🌟🌟⭐⭐'), (4, '🌟🌟🌟🌟⭐'), (5, '🌟🌟🌟🌟🌟')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pid',
            field=models.UUIDField(default='pos977c632653a4', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
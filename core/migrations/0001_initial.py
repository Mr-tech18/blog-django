# Generated by Django 5.0.6 on 2024-09-01 15:09

import core.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.UUIDField(default='cat9fefc1a', primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('category_image', models.ImageField(default='./static/assets/images/1.jpg', upload_to=core.models.get_user_directory_path)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('aid', models.UUIDField(default='catd79488c', primary_key=True, serialize=False, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('rating', models.CharField(choices=[(1, '🌟⭐⭐⭐⭐'), (2, '🌟🌟⭐⭐⭐'), (3, '🌟🌟🌟⭐⭐'), (4, '🌟🌟🌟🌟⭐'), (5, '🌟🌟🌟🌟🌟')], default=1, max_length=2)),
                ('bio', models.TextField(blank=True, null=True)),
                ('author_image', models.ImageField(default='./static/assets/images/1.jpg', upload_to=core.models.get_user_directory_path)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('pid', models.UUIDField(default='poscd44450b7db6', primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('profile_image', models.ImageField(default='./static/assets/images/2.jpg', upload_to=core.models.get_user_directory_path)),
                ('content', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Rating', models.IntegerField(choices=[(1, '🌟⭐⭐⭐⭐'), (2, '🌟🌟⭐⭐⭐'), (3, '🌟🌟🌟⭐⭐'), (4, '🌟🌟🌟🌟⭐'), (5, '🌟🌟🌟🌟🌟')], default=1)),
                ('is_premium', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
            options={
                'ordering': ['-publish', '-created'],
            },
        ),
    ]
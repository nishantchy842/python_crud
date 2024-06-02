# Generated by Django 5.0.6 on 2024-06-02 03:09

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_postmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=225)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blogs.postmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='blogs.usermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

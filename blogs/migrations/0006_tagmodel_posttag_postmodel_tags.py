# Generated by Django 5.0.6 on 2024-06-02 13:20

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_commentmodel_post_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idx', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.postmodel')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.tagmodel')),
            ],
            options={
                'unique_together': {('post', 'tag')},
            },
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(related_name='posts', through='blogs.PostTag', to='blogs.tagmodel'),
        ),
    ]
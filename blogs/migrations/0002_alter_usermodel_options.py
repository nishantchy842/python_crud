# Generated by Django 5.0.6 on 2024-05-31 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name_plural': 'users'},
        ),
    ]

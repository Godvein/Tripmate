# Generated by Django 5.1.2 on 2024-10-28 09:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_blogs_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
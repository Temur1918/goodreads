# Generated by Django 4.0 on 2023-09-14 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_bookreview_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
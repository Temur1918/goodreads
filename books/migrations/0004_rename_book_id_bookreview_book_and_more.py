# Generated by Django 4.0 on 2023-09-21 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_bookreview_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookreview',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='bookreview',
            old_name='user_id',
            new_name='user',
        ),
    ]

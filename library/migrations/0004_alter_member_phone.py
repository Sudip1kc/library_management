# Generated by Django 5.1.6 on 2025-03-08 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_book_author_remove_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-24 10:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True, verbose_name='url'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-26 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_book_book_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_book_quantity', models.IntegerField()),
                ('user_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
        ),
    ]
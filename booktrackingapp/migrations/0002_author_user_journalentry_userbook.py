# Generated by Django 5.1.2 on 2024-11-03 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktrackingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genera', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_entry', models.TextField()),
                ('entry_date', models.DateField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktrackingapp.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktrackingapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktrackingapp.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktrackingapp.user')),
            ],
        ),
    ]
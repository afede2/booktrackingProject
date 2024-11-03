# Generated by Django 5.1.2 on 2024-11-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktrackingapp', '0004_bookstatues_userbook_statues'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='userbook',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]

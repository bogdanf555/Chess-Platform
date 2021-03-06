# Generated by Django 3.2.9 on 2022-01-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0004_user_puzzles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(default='white', max_length=10)),
                ('board_state', models.JSONField()),
                ('moves', models.JSONField()),
            ],
        ),
    ]

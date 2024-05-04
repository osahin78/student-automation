# Generated by Django 5.0.4 on 2024-05-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('stdNumber', models.CharField(max_length=20, unique=True)),
                ('grades', models.JSONField()),
            ],
        ),
    ]

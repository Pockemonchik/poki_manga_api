# Generated by Django 4.1.4 on 2023-05-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.CharField(blank=True, max_length=10, null=True)),
                ('action_type', models.CharField(blank=True, max_length=30, null=True)),
                ('url', models.CharField(blank=True, max_length=60, null=True)),
                ('data', models.TextField(blank=True, null=True)),
                ('query', models.TextField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('object', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Действия пользователей',
                'verbose_name_plural': 'Действия пользователей ',
                'ordering': ['time'],
            },
        ),
    ]

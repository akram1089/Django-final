# Generated by Django 4.2 on 2023-05-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('roll_num', models.CharField(max_length=50)),
                ('stream', models.CharField(max_length=50)),
            ],
        ),
    ]

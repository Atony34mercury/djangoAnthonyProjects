# Generated by Django 4.2 on 2023-04-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
    ]
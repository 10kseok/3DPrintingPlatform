# Generated by Django 4.1.1 on 2022-11-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyer_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('PW', models.CharField(max_length=30)),
                ('TEL', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]

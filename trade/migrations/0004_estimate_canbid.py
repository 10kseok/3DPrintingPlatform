# Generated by Django 4.1.1 on 2022-11-21 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_alter_trade_product_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='canBid',
            field=models.BooleanField(default=True),
        ),
    ]

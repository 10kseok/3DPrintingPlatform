# Generated by Django 4.1.1 on 2022-11-09 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trade',
            name='bid_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trade.bid'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='estimate_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trade.estimate'),
        ),
    ]
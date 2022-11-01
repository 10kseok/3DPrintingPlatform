# Generated by Django 4.1.1 on 2022-11-01 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='seller_id',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='buyer_id',
        ),
        migrations.AlterField(
            model_name='bid',
            name='estimate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.estimate'),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='project_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='trade',
            name='bid_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.bid'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='estimate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.estimate'),
        ),
    ]

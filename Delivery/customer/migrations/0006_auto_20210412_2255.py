# Generated by Django 3.2 on 2021-04-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_ordermodel_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]

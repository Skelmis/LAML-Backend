# Generated by Django 3.2.6 on 2021-08-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_item_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.FloatField(),
        ),
    ]

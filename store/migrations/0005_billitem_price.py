# Generated by Django 2.2 on 2020-06-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_billitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='billitem',
            name='price',
            field=models.FloatField(default=3.6),
            preserve_default=False,
        ),
    ]

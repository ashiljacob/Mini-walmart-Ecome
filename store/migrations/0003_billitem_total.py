# Generated by Django 2.2 on 2020-06-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200630_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='billitem',
            name='total',
            field=models.FloatField(default='23'),
            preserve_default=False,
        ),
    ]
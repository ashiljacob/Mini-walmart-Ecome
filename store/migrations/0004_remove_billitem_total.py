# Generated by Django 2.2 on 2020-06-30 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_billitem_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billitem',
            name='total',
        ),
    ]

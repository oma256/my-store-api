# Generated by Django 4.1 on 2023-05-27 11:22

import apps.seanses.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seanses', '0003_alter_ticket_barcode_alter_ticket_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='uuid',
            field=models.CharField(default=apps.seanses.utils.generate_random_number, editable=False, max_length=13, unique=True, verbose_name='Уникальный ID'),
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-08 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0006_rename_ips_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='tiulo',
            new_name='titulo',
        ),
    ]
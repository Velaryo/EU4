# Generated by Django 4.1.4 on 2022-12-08 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_rename_users_id_proyecto_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='url',
            field=models.URLField(),
        ),
    ]

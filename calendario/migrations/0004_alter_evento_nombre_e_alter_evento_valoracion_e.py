# Generated by Django 4.1.4 on 2023-04-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0003_auto_20220825_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nombre_e',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='evento',
            name='valoracion_e',
            field=models.CharField(choices=[('leve', 'Leve'), ('importante', 'Importante'), ('urgente', 'Urgente')], max_length=10),
        ),
    ]

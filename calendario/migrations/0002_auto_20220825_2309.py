# Generated by Django 3.2 on 2022-08-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='finalizado',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='valoracion',
            field=models.CharField(choices=[('l', 'leve'), ('i', 'importante'), ('u', 'urgente')], max_length=1),
        ),
    ]

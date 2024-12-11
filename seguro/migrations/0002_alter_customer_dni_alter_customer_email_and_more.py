# Generated by Django 4.2.16 on 2024-11-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dni',
            field=models.CharField(max_length=13, unique=True, verbose_name='RUC o Cédula'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='names',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombres'),
        ),
    ]
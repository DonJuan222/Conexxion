# Generated by Django 4.1.4 on 2022-12-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_alter_pago_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='fecha_Vencimiento',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Valido Hasta'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de pago'),
        ),
    ]
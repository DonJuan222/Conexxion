# Generated by Django 4.1.3 on 2022-12-02 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_cliente_fecha_instalacion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='agenda',
            new_name='pago',
        ),
        migrations.AlterModelOptions(
            name='pago',
            options={'verbose_name': 'Pago', 'verbose_name_plural': 'Pagos'},
        ),
        migrations.AlterModelTable(
            name='pago',
            table='Pago',
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0011_alter_cliente_mensualidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='status',
            field=models.CharField(blank=True, choices=[('arriba', 'Activo'), ('abajo', 'Sin servicio')], max_length=20, null=True, verbose_name='Estado'),
        ),
    ]
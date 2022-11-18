# Generated by Django 4.1.3 on 2022-11-18 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0003_remove_cliente_fecha_instalacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('valor_Pago', models.IntegerField(verbose_name='Valor de pago')),
                ('fecha_Pago', models.DateTimeField(verbose_name='Fecha de Pago')),
                ('valido', models.DateTimeField(verbose_name='Valido Hasta')),
                ('fecha_Instalacion', models.DateField(verbose_name='Fecha de Instalacion')),
                ('cliente_rela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Id_Soporte', to='cliente.cliente')),
            ],
        ),
    ]

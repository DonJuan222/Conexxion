# Generated by Django 4.1.3 on 2022-11-26 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripciones')),
                ('valor_Pago', models.CharField(max_length=200, verbose_name='Valor del Pago')),
                ('fecha_pago', models.DateTimeField(null=True, verbose_name='Fecha de pago')),
                ('fecha_Vencimiento', models.DateTimeField(null=True, verbose_name='Valido Hasta')),
                ('fecha_Instalacion', models.DateField(null=True, verbose_name='Fecha de Instalacion')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
                'db_table': 'Agenda',
            },
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='Ip del Cliente')),
                ('cedula', models.CharField(max_length=12, verbose_name='Cedula del Cliente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Cliente')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido del Cliente')),
                ('telefono_uno', models.CharField(max_length=12, verbose_name='Primer Telefono ')),
                ('telefonos_dos', models.CharField(blank=True, max_length=12, null=True, verbose_name='Segundo Telefono')),
                ('mensualidad', models.CharField(max_length=100, null=True, verbose_name='Mensualidad')),
                ('agenda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.agenda', verbose_name='Datos de Pago')),
                ('id_Estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Estado', to='home.estado')),
                ('id_Municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Municipio', to='home.municipio')),
                ('id_lugar_Residencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Residencia', to='home.lugar_residencia')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': ['ip'],
            },
        ),
    ]

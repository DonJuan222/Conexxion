# Generated by Django 4.1.3 on 2022-11-02 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_alter_lugar_residencia_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('ip', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=15, null=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Cliente')),
                ('telefono_uno', models.CharField(max_length=12, verbose_name='Primer Telefono ')),
                ('telefonos_dos', models.CharField(blank=True, max_length=12, null=True, verbose_name='Segundo Telefono')),
                ('mensualidad', models.CharField(max_length=100, null=True, verbose_name='Mensualidad')),
                ('fecha_Instalacion', models.DateField(verbose_name='Fecha de Instalacion')),
                ('id_Cartera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Id_Cartera', to=settings.AUTH_USER_MODEL)),
                ('id_Estado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Id_Estado', to='home.estado')),
                ('id_Municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Id_Municipio', to='home.municipio')),
                ('id_lugar_Residencia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Id_Residencia', to='home.lugar_residencia')),
                ('id_soporte_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Id_Soporte', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': ['ip'],
            },
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_cliente_fecha_instalacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado'),
        ),
    ]
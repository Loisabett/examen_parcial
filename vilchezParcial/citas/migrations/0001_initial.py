# Generated by Django 4.2.1 on 2023-06-04 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_nombre', models.CharField(max_length=255)),
                ('doctor_direccion', models.CharField(max_length=255)),
                ('doctor_telefono', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'doctores',
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad_nombre', models.CharField(max_length=55)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'especialidades',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumentoIdentidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento_nombre', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tipos_documentos_identidades',
            },
        ),
        migrations.CreateModel(
            name='TipoSeguro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_seguro_nombre', models.CharField(max_length=85)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tipos_seguros',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(blank=True, null=True)),
                ('direccion', models.CharField(default=False)),
                ('fecha_nacimiento', models.CharField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tipo_documento_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.tipodocumentoidentidad')),
                ('tipo_seguro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.tiposeguro')),
            ],
            options={
                'db_table': 'pacientes',
            },
        ),
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.CharField(max_length=85)),
                ('observaciones', models.CharField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('especialidad_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.especialidad')),
                ('paciente_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.paciente')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'citas_medicas',
            },
        ),
    ]
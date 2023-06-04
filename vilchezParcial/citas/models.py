from django.db import models
from django.contrib.auth.models import User
from users.models import Usuario

class TipoDocumentoIdentidad(models.Model):
   tipo_documento_nombre = models.CharField(max_length=255)
   created_at = models.DateTimeField(auto_now_add=True)
  
   def __str__(self):
       return self.tipo_documento_nombre
  
   class Meta:
       db_table = "tipos_documentos_identidades"

class TipoSeguro(models.Model):
   tipo_seguro_nombre = models.CharField(max_length=85)
   created_at = models.DateTimeField(auto_now_add=True)
  
   def __str__(self):
       return self.tipo_seguro_nombre
  
   class Meta:
       db_table = "tipos_seguros"

class Especialidad(models.Model):
   especialidad_nombre = models.CharField(max_length=55)
   created_at = models.DateTimeField(auto_now_add=True)
  
   def __str__(self):
       return self.especialidad_nombre
  
   class Meta:
       db_table = "especialidades"

class Doctor(models.Model):
   doctor_nombre = models.CharField(max_length=255)
   doctor_direccion = models.CharField(max_length=255)
   doctor_telefono = models.CharField(max_length=10)
   created_at = models.DateTimeField(auto_now_add=True)
  
   def __str__(self):
       return self.doctor_nombre
  
   class Meta:
       db_table = "doctores"

class Paciente(models.Model):
   nombres = models.CharField(max_length=255)
   apellidos = models.CharField(null=True, blank=True)
   direccion = models.CharField(default=False)
   nro_documento = models.CharField(default=False)
   fecha_nacimiento = models.CharField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)
   tipo_documento_id = models.ForeignKey(TipoDocumentoIdentidad,on_delete=models.CASCADE, null=True, blank=True)
   tipo_seguro = models.ForeignKey(TipoSeguro,on_delete=models.CASCADE, null=True, blank=True)
  
   def __str__(self):
       return self.nombres
  
   class Meta:
       db_table = "pacientes"

class CitaMedica(models.Model):
   fecha_cita = models.CharField(max_length=85)
   observaciones = models.CharField(null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   paciente_id = models.ForeignKey(Paciente,on_delete=models.CASCADE, null=True, blank=True)
   doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True, blank=True)
   especialidad_id = models.ForeignKey(Especialidad,on_delete=models.CASCADE, null=True, blank=True)
   username = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, blank=True)
  
   def __str__(self):
       return self.fecha_cita
  
   class Meta:
       db_table = "citas_medicas"

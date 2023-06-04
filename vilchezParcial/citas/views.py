from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TipoDocumentoIdentidad, TipoSeguro, Paciente, Especialidad, Doctor, CitaMedica
from django.urls import reverse_lazy
from django.contrib import messages
from django import forms

# Create your views here.
def home(request):
    return render(request, 'home.html')

class documentoList(ListView):
    model = TipoDocumentoIdentidad
    context_object_name = "tipodocumento"
    template_name = "citas/documento_list.html"
    
class documentoCreate(CreateView):
    model = TipoDocumentoIdentidad
    fields = ["tipo_documento_nombre"]
    success_url = reverse_lazy("tipodocumento")
    template_name = "citas/documento_form.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El documento fue creado correctamente.")
        return super(documentoCreate, self).form_valid(form)

class documentoUpdate(UpdateView):
    model = TipoDocumentoIdentidad
    fields = ["tipo_documento_nombre"]
    success_url = reverse_lazy("tipodocumento")
    template_name = "citas/documento_form.html"

    def form_valid(self, form):
        messages.success(self.request, "El documento fue actualizado correctamente.")
        return super(documentoUpdate, self).form_valid(form)
    
class documentoDelete(DeleteView):
    model = TipoDocumentoIdentidad
    success_url = reverse_lazy("tipodocumento")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "El documento fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class seguroList(ListView):
    model = TipoSeguro
    context_object_name = "tiposeguro"
    template_name = "citas/seguro_list.html"
    
class seguroCreate(CreateView):
    model = TipoSeguro
    fields = ["tipo_seguro_nombre"]
    success_url = reverse_lazy("tiposeguro")
    template_name = "citas/seguro_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El Seguro fue creado correctamente.")
        return super(seguroCreate, self).form_valid(form)

class seguroUpdate(UpdateView):
    model = TipoSeguro
    fields = ["tipo_seguro_nombre"]
    success_url = reverse_lazy("tiposeguro")
    template_name = "citas/seguro_form.html"

    def form_valid(self, form):
        messages.success(self.request, "El Seguro fue actualizado correctamente.")
        return super(seguroUpdate, self).form_valid(form)
    
class seguroDelete(DeleteView):
    model = TipoSeguro
    success_url = reverse_lazy("tiposeguro")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "El Seguro fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class PacienteList(ListView):
    model = Paciente
    context_object_name = "paciente"
    template_name = "citas/paciente_list.html"

class pacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["nombres", "apellidos", "direccion", "nro_documento", "fecha_nacimiento", "tipo_documento_id", "tipo_seguro"]
        template_name = "citas/paciente_form.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_seguro'].label_from_instance = lambda obj: obj.tipo_seguro_nombre
        self.fields['tipo_documento_id'].label_from_instance = lambda obj: obj.tipo_documento_nombre

class PacienteCreate(CreateView):
    model = Paciente
    form_class = pacienteForm
    success_url = reverse_lazy("paciente")
    template_name = "citas/paciente_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El paciente fue creado correctamente.")
        return super().form_valid(form)
    
class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = pacienteForm
    success_url = reverse_lazy("paciente")

    def form_valid(self, form):
        messages.success(self.request, "El paciente fue actualizado correctamente.")
        return super(PacienteUpdate, self).form_valid(form)
    
class PacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy("paciente")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "El paciente fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class especialidadesList(ListView):
    model = Especialidad
    context_object_name = "especialidades"
    template_name = "especialidades_list.html"
    
class especialidadesCreate(CreateView):
    model = Especialidad
    fields = ["especialidad_nombre"]
    success_url = reverse_lazy("especialidades")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La especialidad fue creado correctamente.")
        return super(especialidadesCreate, self).form_valid(form)
    
class especialidadesUpdate(UpdateView):
    model = Especialidad
    fields = ["especialidad_nombre"]
    success_url = reverse_lazy("especialidades")

    def form_valid(self, form):
        messages.success(self.request, "La especialidad fue actualizado correctamente.")
        return super(especialidadesUpdate, self).form_valid(form)
    
class especialidadesDelete(DeleteView):
    model = Especialidad
    success_url = reverse_lazy("especialidades")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "La especialidad fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class doctorList(ListView):
    model = Doctor
    context_object_name = "doctores"
    template_name = "citas/doctor_list.html"
    
class doctorCreate(CreateView):
    model = Doctor
    fields = ["doctor_nombre","doctor_direccion","doctor_telefono"]
    success_url = reverse_lazy("doctores")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "El doctor fue creado correctamente.")
        return super(doctorCreate, self).form_valid(form)
    
class doctorUpdate(UpdateView):
    model = Doctor
    fields = ["doctor_nombre","doctor_direccion","doctor_telefono"]
    success_url = reverse_lazy("doctores")

    def form_valid(self, form):
        messages.success(self.request, "El doctor fue actualizado correctamente.")
        return super(doctorUpdate, self).form_valid(form)
    
class doctorDelete(DeleteView):
    model = Doctor
    success_url = reverse_lazy("doctores")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "El doctor fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
class citasList(ListView):
    model = CitaMedica
    context_object_name = "citas"
    template_name = "citas/citas_list.html"

class citasForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ["fecha_cita","observaciones",  "especialidad_id", "doctor_id", "paciente_id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['especialidad_id'].label_from_instance = lambda obj: obj.especialidad_nombre
        self.fields['doctor_id'].label_from_instance = lambda obj: obj.doctor_nombre
        self.fields['paciente_id'].label_from_instance = lambda obj: obj.nombres

class citasCreate(CreateView):
    model = CitaMedica
    form_class = citasForm
    success_url = reverse_lazy("citas")
    template_name = "citas/citas_form.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La cita fue creado correctamente.")
        return super().form_valid(form)
    
class citasUpdate(UpdateView):
    model = CitaMedica
    form_class = citasForm
    success_url = reverse_lazy("citas")
    template_name = "citas/citas_form.html"
    
    def form_valid(self, form):
        messages.success(self.request, "La cita fue actualizado correctamente.")
        return super(citasUpdate, self).form_valid(form)
    
class citasDelete(DeleteView):
    model = CitaMedica
    success_url = reverse_lazy("citas")

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, "La cita fue eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
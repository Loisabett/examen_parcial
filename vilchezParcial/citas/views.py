from django.shortcuts import render
from django.views.generic.list import ListView, CreateView, UpdateView
from .models import TipoDocumentoIdentidad
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

class TipoDocumentoIdentidadList(ListView):
    model = TipoDocumentoIdentidad
    context_object_name = 'tipos_documentos_identidades'

class TipoDocumentoIdentidadCreate(CreateView):
    model = TipoDocumentoIdentidad
    fields = ['tipo_documento_nombre']
    success_url = reverse_lazy('tipos_documentos_identidades')
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "La cita fue creada correctamente.")
        return super(TipoDocumentoIdentidadCreate,self).form_valid(form)
    
class TipoDocumentoIdentidadUpdate(UpdateView):
    model = TipoDocumentoIdentidad
    fields = ['tipo_documento_nombre']
    success_url = reverse_lazy('tipos_documentos_identidades')
    
    def form_valid(self, form):
        messages.success(self.request, "La tabla fue actualizada correctamente.")
        return super(TipoDocumentoIdentidadUpdate,self).form_valid(form)
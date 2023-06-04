from django.urls import path
from .views import home, TipoDocumentoIdentidadList, TipoDocumentoIdentidadCreate, TipoDocumentoIdentidadUpdate

urlpatterns = [
    path('', home, name='home'),
    path('tipos_documentos_identidades/', TipoDocumentoIdentidadList.as_view(),name='tipos_documentos_identidades'),
    path('tipo_documento_identidad/create/', TipoDocumentoIdentidadCreate.as_view(),name='tipo_documento_identidad-create'),
    path('tipo_documento_identidad/update/<int:pk>/', TipoDocumentoIdentidadUpdate.as_view(),name='tipo_documento_identidad-update'),
]
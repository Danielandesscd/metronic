from django.urls import path

from formulario.views import FormularioView
app_name = 'formulario'

urlpatterns = [
    # ...

    path('', FormularioView.as_view(template_name = 'pages/formulario/formulario.html'), name='formulario'),

    # ...
]
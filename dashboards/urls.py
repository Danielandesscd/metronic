from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from dashboards.views import DashboardsView
from auth.signin.views import AuthSigninView
from formulario.views import FormularioView
app_name = 'dashboards'

urlpatterns = [
    path('', AuthSigninView.as_view(template_name ='pages/auth/signin.html'), name='signin'),
    #path('', AuthSigninView.as_view(template_name ='pages/auth/signin.html'), name='signin'),


    path('index', DashboardsView.as_view(template_name ='pages/dashboards/index.html'), name='index'),

    path('home', DashboardsView.as_view(template_name ='pages/dashboards/home.html'), name='home'),



    path('error', DashboardsView.as_view(template_name = 'non-exist-file.html'), name='Error Page'),
    # Mypage urls
    path('formulario', FormularioView.as_view(template_name = 'formulario..html'), name='formulario'),

]
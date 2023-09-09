from django.urls import path

from .import views
app_name = 'skbankapp'


urlpatterns = [
    path('', views.demo, name='demo'),
    path('register', views.devolep, name='register'),
    path('login', views.login, name='login'),
    path('register', views.devolep, name='register'),
    path('register', views.devolep, name='register'),
    path('Button', views.login, name='Button'),
    path('logout', views.logout, name='logout'),
    path('message_form', views.message_form, name='message_form'),




]

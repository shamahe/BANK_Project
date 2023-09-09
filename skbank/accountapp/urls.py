from django.urls import path
from . import views
app_name = 'accountapp'
urlpatterns = [

    path('', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-branches/', views.load_cities, name='ajax_load_branches'),
    path('logout', views.logout, name='logout'),
    path('add/contact_form', views.contact_form, name='contact_form'),
]

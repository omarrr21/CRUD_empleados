from django.contrib import admin
from django.urls import path
from . import views

app_name='persona_app'
urlpatterns = [
    path('listaemp/',views.ListAllemp.as_view(),name='empleados_all'),
    path('byarea/',views.Listbyarea.as_view()),
    path('byarea/<sho>/',views.Listbyarea.as_view(),name='emparea'),
    path('buscaemp/',views.Listempbykey.as_view()),
    path('porhab/',views.Listahabilidades.as_view()),
    path('veremp/<pk>',views.Detemp.as_view(),name='detalle'),
    path('add/',views.Createmp.as_view(),name='nuevoemp'),
    path('succes/',views.Succesview.as_view(),name='correct'),

    path('update/<pk>', views.Updatemp.as_view(),name='modificar'),
    path('delete/<pk>',views.Deletemp.as_view(),name='del'),
    path('', views.Inicioview.as_view(),name='inicio'),
    path('listadmin/', views.Listadmin.as_view(),name='listadmin'),

]
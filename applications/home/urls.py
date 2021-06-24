from django.contrib import admin
from django.urls import path
from . import views
app_name='pruebas'
urlpatterns = [
    path('prueba/',views.PruebaView.as_view()),
    path('lista/',views.PruebaListview.as_view()),
    path('add/', views.Createprueba.as_view(),name='crear'),
    path('home/',views.Home.as_view()),
]
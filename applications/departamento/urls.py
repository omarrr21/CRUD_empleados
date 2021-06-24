from django.contrib import admin
from django.urls import path
from . import views
app_name='depa_app'
urlpatterns = [
    path('newdep/',views.Newregdep.as_view(),name='nuevodep'),
    path('listdep/', views.Deplist.as_view(), name='depalist'),
]
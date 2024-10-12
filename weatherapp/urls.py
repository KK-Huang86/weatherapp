from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data,name="get_data"),
    path('notify/',views.line_notify,name="line_notify")
]

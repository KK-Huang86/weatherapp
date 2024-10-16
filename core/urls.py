from django.contrib import admin
from django.urls import path,include
from lib.utils.env import is_dev
from debug_toolbar.toolbar import debug_toolbar_urls



urlpatterns = [
    path("",include("weatherapp.urls")),
    path("admin/", admin.site.urls),
]

if is_dev():
    urlpatterns += debug_toolbar_urls()
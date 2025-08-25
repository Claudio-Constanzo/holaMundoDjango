from django.contrib import admin
from django.urls import path
from firstApp.views import display
from firstApp.views import displayDateTime

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola1/",display),
    path("ahora/", displayDateTime),
]

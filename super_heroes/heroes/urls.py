from heroes.views import lista_familia
from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('lista_familia/', lista_familia),
    path('admin/', admin.site.urls),
]


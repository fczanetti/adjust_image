from django.urls import path
from adjust_image.base import views


app_name = "base"
urlpatterns = [
    path('', views.imagem, name="imagem")
]

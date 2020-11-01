from django.urls import path

from . import views

urlpatterns = [
    path('', views.portrait_image_view, name='index'),
    path('success/', views.success, name='success')
]
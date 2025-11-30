from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tareas/<int:task_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('tareas/agregar/', views.agregar_tarea, name='agregar_tarea'),
    path('tareas/<int:task_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]

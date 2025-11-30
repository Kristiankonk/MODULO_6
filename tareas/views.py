
# Create your views here.
from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

from .forms import TareaForm, RegistroForm

# Diccionario global: { user_id: [ {id, titulo, descripcion}, ... ] }
tareas_por_usuario = defaultdict(list)
siguiente_id_por_usuario = defaultdict(int)


def _obtener_siguiente_id(user_id):
    siguiente_id_por_usuario[user_id] += 1
    return siguiente_id_por_usuario[user_id]


def _obtener_tarea_o_404(user_id, task_id):
    for tarea in tareas_por_usuario[user_id]:
        if tarea["id"] == task_id:
            return tarea
    raise Http404("Tarea no encontrada")


# AUTENTICACIÓN 

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registrar/registro.html', {'form': form})


# VISTAS DE TAREAS 

@login_required
def lista_tareas(request):
    user_id = request.user.id
    tareas = tareas_por_usuario[user_id]
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})


@login_required
def detalle_tarea(request, task_id):
    user_id = request.user.id
    tarea = _obtener_tarea_o_404(user_id, task_id)
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})


@login_required
def agregar_tarea(request):
    user_id = request.user.id

    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            nueva_tarea = {
                "id": _obtener_siguiente_id(user_id),
                "titulo": form.cleaned_data["titulo"],
                "descripcion": form.cleaned_data["descripcion"],
            }
            tareas_por_usuario[user_id].append(nueva_tarea)
            return redirect('lista_tareas')
    else:
        form = TareaForm()

    return render(request, 'tareas/agregar_tarea.html', {'form': form})


@login_required
def eliminar_tarea(request, task_id):
    user_id = request.user.id
    tarea = _obtener_tarea_o_404(user_id, task_id)

    if request.method == "POST":
        # eliminar
        tareas_por_usuario[user_id] = [
            t for t in tareas_por_usuario[user_id] if t["id"] != task_id
        ]
        return redirect('lista_tareas')

    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})

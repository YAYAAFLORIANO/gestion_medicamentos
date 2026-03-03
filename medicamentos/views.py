from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento
from .forms import MedicamentoForm

def lista_medicamentos(request):
    query = request.GET.get('q')
    medicamentos = Medicamento.objects.all()

    if query:
        medicamentos = medicamentos.filter(nombre__icontains=query)

    total = medicamentos.count()
    bajos = medicamentos.filter(stock_minimo__lte=10).count()

    return render(request, 'lista.html', {
        'medicamentos': medicamentos,
        'total': total,
        'bajos': bajos
    })

def crear_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = MedicamentoForm()

    return render(request, 'formulario.html', {
        'form': form,
        'titulo': 'Agregar Medicamento'
    })

def editar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)

    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = MedicamentoForm(instance=medicamento)

    return render(request, 'formulario.html', {
        'form': form,
        'titulo': 'Editar Medicamento'
    })

def eliminar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)

    if request.method == 'POST':
        medicamento.delete()
        return redirect('lista')

    return render(request, 'eliminar.html', {'medicamento': medicamento})
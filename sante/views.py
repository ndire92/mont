from django.shortcuts import render, redirect
from sante import ReproductionEtJeune

from sante.PlanificationF import PLANFF
from sante.ReproductionEtJeune import reprojeu
from sante.SantePaludisme import santePalu
from sante.SurvieEnfant import survienf
from sante.VaccinationEtRoutine import vacin

from sante.models import *
# Create your views here.


def pltfm(request):
    if request.method == 'POST':
        form = PLANFF(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sante/PlanificationFamiliale/')
    else:
        form = PLANFF()
        return render(request, 'sante/PlanificationFamiliale.html', {'form': form, 'dataObject': PlanificationFamiliale.objects.all()})


# update equipement
def update_P(request, id):
    dataP = PlanificationFamiliale.objects.get(id=id)
    form = PLANFF(instance=dataP)
    if request.method == 'POST':
        form = PLANFF(request.POST, instance=dataP)
        if form.is_valid():
            form.save()
            return redirect('/sante/PlanificationFamiliale/')

    context = {

        'form': form,

    }
    return render(request, 'sante/PlanificationFamiliale.html', context)

# delete pla famm


def delete_P(request, id):
    dataP = PlanificationFamiliale.objects.get(id=id)
    if request.method == 'POST':
        dataP.delete()
        return redirect('/sante/PlanificationFamiliale/')
    context = {

        'item': dataP, }
    return render(request, 'sante/delete_pl.html', context)


def repjeu(request):
    if request.method == 'POST':
        form = reprojeu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sante/ReproductionEtJeune/')
    else:
        form = reprojeu()
        return render(request, 'sante/ReproductionEtJeune.html', {'form': form, 'dataObject': ReproductionEtJeune.objects.all()})


# update equipement
def update_repro(request, id):
    dataP = ReproductionEtJeune.objects.get(id=id)
    form = reprojeu(instance=dataP)
    if request.method == 'POST':
        form = reprojeu(request.POST, instance=dataP)
        if form.is_valid():
            form.save()
            return redirect('/sante/ReproductionEtJeune/')

    context = {

        'form': form,

    }
    return render(request, 'sante/ReproductionEtJeune.html', context)

# delete pla famm


def delete_repro(request, id):
    dataP = ReproductionEtJeune.objects.get(id=id)
    if request.method == 'POST':
        dataP.delete()
        return redirect('/sante/ReproductionEtJeune/')
    context = {

        'item': dataP, }
    return render(request, 'sante/delete_rep.html', context)

# santepalu


def spld(request):
    if request.method == 'POST':
        form = santePalu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sante/SantePaludisme/')
    else:
        form = santePalu()
        return render(request, 'sante/SantePaludisme.html', {'form': form, 'dataObject': SantePaludisme.objects.all()})


# update palu
def update_palu(request, id):
    dataP = SantePaludisme.objects.get(id=id)
    form = santePalu(instance=dataP)
    if request.method == 'POST':
        form = santePalu(request.POST, instance=dataP)
        if form.is_valid():
            form.save()
            return redirect('/sante/SantePaludisme/')

    context = {

        'form': form,

    }
    return render(request, 'sante/SantePaludisme.html', context)

# delete palu famm


def delete_palu(request, id):
    dataP = SantePaludisme.objects.get(id=id)
    if request.method == 'POST':
        dataP.delete()
        return redirect('/sante/SantePaludisme/')
    context = {

        'item': dataP, }
    return render(request, 'sante/delete_palu.html', context)


# survie enfa


def survie(request):
    if request.method == 'POST':
        form = survienf(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sante/survienfant/')
    else:
        form = survienf()
        return render(request, 'sante/survienfant.html', {'form': form, 'dataObject': SurvieEnfant.objects.all()})


# update palu
def update_vie(request, id):
    dataObject = SurvieEnfant.objects.get(id=id)
    form = survienf(instance=dataObject)
    if request.method == 'POST':
        form = survienf(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            return redirect('/sante/survienfant/')

    context = {

        'form': form,

    }
    return render(request, 'sante/survienfant.html', context)

# delete palu famm


def delete_vie(request, id):
    dataP = SurvieEnfant.objects.get(id=id)
    if request.method == 'POST':
        dataP.delete()
        return redirect('/sante/survienfant/')
    context = {

        'item': dataP, }
    return render(request, 'sante/delete_survienfant.html', context)


# vacci


def vaci(request):
    if request.method == 'POST':
        form = vacin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sante/vacination/')
    else:
        form = vacin()
        return render(request, 'sante/vaci.html', {'form': form, 'dataObject': VaccinationEtRoutine.objects.all()})


# update palu
def update_vaci(request, id):
    dataObject = VaccinationEtRoutine.objects.get(id=id)
    form = vacin(instance=dataObject)
    if request.method == 'POST':
        form = vacin(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            return redirect('/sante/vacination/')

    context = {

        'form': form,

    }
    return render(request, 'sante/vaci.html', context)

# delete palu famm


def delete_vaci(request, id):
    dataP = VaccinationEtRoutine.objects.get(id=id)
    if request.method == 'POST':
        dataP.delete()
        return redirect('/sante/vacination/')
    context = {

        'item': dataP, }
    return render(request, 'sante/delete_vaci.html', context)

from django.shortcuts import render, redirect
from education.DimPer import DPRF
from education.DimPers import DPR
from education.DimEqui import equi
from education.DimG import Dg
from education.dimass import acc
from django.contrib import messages

from education.models import DimEduc_Equipements, DimEduc_Gouvernance, DimEduc_Personnel, DimEduc_Perfomance, DimEduc_Access

# Create your views here.


def DimEq(request):
    if request.method == 'POST':
        form = equi(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/education/DimEqui/')
    else:
        form = equi()
        return render(request, 'edu/equipement.html', {'form': form, 'dataObject': DimEduc_Equipements.objects.all()})

# update equipement


def update_eq(request, id):
    dO = DimEduc_Equipements.objects.get(id=id)
    form = equi(instance=dO)
    if request.method == 'POST':
        form = equi(request.POST, instance = dO)
        if form.is_valid():
            form.save()
            return redirect('/education/DimEqui/')

    context = {

        'form': form,

    }
    return render(request, 'edu/equipement.html', context)

# delete equipement


def delete_eq(request, id):
    dataObject = DimEduc_Equipements.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/education/DimEqui/')
    context = {

        'item': dataObject, }
    return render(request, 'edu/delete_DimEqui.html', context)


def DG(request):
    if request.method == 'POST':
        form = Dg(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/education/DimGou/')
    else:
        form = Dg()

    return render(request, 'edu/gouver.html', {'form': form, 'dataObject': DimEduc_Gouvernance.objects.all()})

# update gouvernance


def update_gv(request, id):
    dataObje = DimEduc_Gouvernance.objects.get(id=id)
    form = Dg(instance=dataObje)
    if request.method == 'POST':
        form = Dg(request.POST, instance=dataObje)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/education/DimGou/')

    context = {

        'form': form,

    }
    return render(request, 'edu/gouver.html', context)

# delete equipement


def delete_gv(request, id):
    dataObje = DimEduc_Gouvernance.objects.get(id=id)
    if request.method == 'POST':
        dataObje.delete()
        return redirect('/education/DimGou/')
    context = {

        'item': dataObje, }
    return render(request, 'edu/delete_gv.html', context)


def person(request):
    if request.method == 'POST':
        form = DPR(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/education/Dimp/')
    else:
        form = DPR()

    return render(request, 'edu/perso.html', {'form': form, 'dataObject': DimEduc_Personnel.objects.all()})


# update personnel
def update_perso(request, id):
    dataObj = DimEduc_Personnel.objects.get(id=id)
    form = DPR(instance=dataObj)
    if request.method == 'POST':
        form = DPR(request.POST, instance=dataObj)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/education/Dimp/')

    context = {

        'form': form,

    }
    return render(request, 'edu/perso.html', context)

# delete personnel


def delete_perso(request, id):
    dataObj = DimEduc_Personnel.objects.get(id=id)
    if request.method == 'POST':
        dataObj.delete()
        return redirect('/education/Dimp/')
    context = {

        'item': dataObj, }
    return render(request, 'edu/delete_perso.html', context)


def DP(request):
    if request.method == 'POST':
        form = DPRF(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/education/DimPer/')
    else:
        form = DPRF()

    return render(request, 'edu/perfor.html', {'form': form, 'dataObject': DimEduc_Perfomance.objects.all()})


# update perfor
def update_perfor(request, id):
    dataObject = DimEduc_Perfomance.objects.get(id=id)
    form = DPRF(instance=dataObject)
    if request.method == 'POST':
        form = DPRF(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, ' succefully ')
            return redirect('/education/DimPer/')

    context = {

        'form': form,

    }
    return render(request, 'edu/perfor.html', context)

# delete perfor


def delete_perfor(request, id):
    da = DimEduc_Perfomance.objects.get(id=id)
    if request.method == 'POST':
        da.delete()
        return redirect('/education/DimPer/')
    context = {

        'item': da, }
    return render(request, 'edu/delete_perfo.html', context)


def dis(request):
    if request.method == 'POST':
        form = acc(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/education/dim_Access/')
    else:
        form = acc()
    return render(request, 'edu/dimdass.html', {'form': form, 'dbacess': DimEduc_Access.objects.all()})


# update perfor
def update_acc(request, id):
    dataPerf = DimEduc_Access.objects.get(id=id)
    form = acc(instance=dataPerf)
    if request.method == 'POST':
        form = acc(request.POST, instance=dataPerf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/education/dim_Access/')

    context = {

        'form': form,

    }
    return render(request, 'edu/dimdass.html', context)

# delete perfor


def delete_acc(request, id):
    dataPerf = DimEduc_Access.objects.get(id=id)
    if request.method == 'POST':
        dataPerf.delete()
        return redirect('/education/dim_Access/')
    context = {

        'item': dataPerf, }
    return render(request, 'edu/delete.html', context)

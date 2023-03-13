
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# from django.template import engine
# from django.template import Engine, EngineHandler, engines
from app.models import CustomUser
from django.contrib import messages

from education.models import DimEduc_Equipements, DimEduc_Gouvernance, DimEduc_Personnel, DimEduc_Perfomance, DimEduc_Access

from sante.models import PlanificationFamiliale, Visiteur, ReproductionEtJeune, SantePaludisme, SurvieEnfant, VaccinationEtRoutine


# @login_required(login_url='/')
def Home(request):
    plan = PlanificationFamiliale.objects.all().count()
    repro = ReproductionEtJeune.objects.all().count()
    palu = SantePaludisme.objects.all().count()
    survie = SurvieEnfant.objects.all().count()
    vacc = VaccinationEtRoutine.objects.all().count()
    nb_visite = Visiteur.objects.all().count()
    # educ
    dimequ = DimEduc_Equipements.objects.all().count()
    dimgou = DimEduc_Gouvernance.objects.all().count()
    dimper = DimEduc_Personnel.objects.all().count()
    dimperf = DimEduc_Perfomance.objects.all().count()
    dimacc = DimEduc_Access.objects.all().count()

    context = {
        'plan ': plan,
        'repro': repro,
        'palu': palu,
        'survie': survie,
        'vacc': vacc,
        'nb_visite': nb_visite,
        'dimequ': dimequ,
        'dimgou ': dimgou,
        'dimper': dimper,
        'dimperf': dimperf,
        'dimacc': dimacc,

    }

    return render(request, 'Hod/home.html', context)

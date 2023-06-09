# Generated by Django 4.1.6 on 2023-03-13 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GouvernanceSante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('NomDistrict', models.CharField(max_length=250)),
                ('DepensFonctment', models.IntegerField()),
                ('DepensInvistisnt', models.IntegerField()),
                ('MassSalarial', models.IntegerField()),
                ('PersMedical', models.IntegerField()),
                ('PersAppui', models.IntegerField()),
                ('MasSalarialPersSanitairAppui', models.IntegerField()),
                ('DepensEauDomainSante', models.IntegerField()),
                ('DepensElectDomainSante', models.IntegerField()),
                ('AchatMedicaAidSocial', models.IntegerField()),
                ('TotDepensSant', models.IntegerField()),
                ('DepensInvestisSant', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanificationFamiliale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('NomDistrict', models.CharField(max_length=250)),
                ('TxRecrutementPF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxdAbandonPF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TotAbandonsPF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagF15a49ansSMCapresAvortt', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctageUtilisacPF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PcetageUtilisatPF_15a49ans', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxPrevalencContraceptv', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ReproductionEtJeune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('NomDistrict', models.CharField(max_length=250)),
                ('PctagAdo15a19anSousMC_aprAvort', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagAdo20a24anSousMC_AprAvort', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagAvortAdo15a19anPEC_AmiuAuPT', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagAvortF20a24anPEC_AuPTMisoprostol', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagAvortAdo20a24anPEC_AmiuAuPT', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagAvortAdo15a19anPEC_AuPTMisoprostol', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagAccouchAdo15a19an_AssistPerQalifi', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagAccouchAdo20a24an_AssistPersQalifie', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PctagUtilisatc_PF_15a49ans', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SanteAlimentationEtNutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('NomDistrict', models.CharField(max_length=250)),
                ('PtgEnftDemoins5anAyantInsuffisPonderal1', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgFEnceintesPresentantAnemie', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnfmoins5anAyantInsuffisPonderal', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftmoin5anAyantInsuffisPonderalModere', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftmoin5ansAyantInsuffisPonderalGrav', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftmoin5anAyanInsuffisPonderalGlobal', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftmoin5anAyantMASsansComplication', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftmoin5anSouffranMAM', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftMoin5anDepistMalnutriAigu', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgFEnceintPresentMalnutriAigu', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftMoins5anPresentAnemi', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftmoin5anAyantRetardCSeverTA', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnftMoin5anAyantRetarCroissancTA', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxAbandonEnftMoin5anMASAuCREN', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnft6a59moisDepistMAM', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NvxAdmissionLieRechutCREN', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NvxAdmissionLieRechutUREN', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxGuerisonEnft6a59MoisMASaLUREN', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TTEnftsMAM6a59MoisDepistes', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxDeGuerisonUREN', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PptEnftMoins5anSouffranMAM', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxDeMASTraitAvecSuccesAuCREN', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PptEnftMoins5anAyantInsuffisPS', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PptEnftMoins5anMASGueri', models.DecimalField(decimal_places=5, max_digits=10)),
                ('MalnutChronic_RetarCSeverTA', models.DecimalField(decimal_places=5, max_digits=10)),
                ('MalnutChronicO_RetardCMTA', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SantePaludisme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('NomDistrict', models.CharField(max_length=250)),
                ('TxMorbiditPptnellPalustreTTAge', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxMorbiditPptnellPalustreFEnceint', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxmorbiditPptnellePalustrMoins5ans', models.DecimalField(decimal_places=5, max_digits=10)),
                ('IncidencPaludism_1000Habts', models.DecimalField(decimal_places=5, max_digits=10)),
                ('IncidencPaludismgGravTT', models.DecimalField(decimal_places=5, max_digits=10)),
                ('CasPaludismConfirmTT', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NbreTTCasPaluSimplConfirmInsttTRecuTaitemt', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SurvieEnfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('NomDistrict', models.CharField(max_length=250)),
                ('PtgEnft0a59MoisAyantDiarrhe', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PptCasPneuMoni0a59Mois', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PptEnftPneumoniGravSaturatO2Mesure', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PptEnft0a59MoisSouffranAnemi', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PptEnft0a59moisPresenttAnemi', models.DecimalField(decimal_places=5, max_digits=10)),
                ('CasEnftMoins5ansBSoignCtrDiarrhCentr', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NbreCasDiarrhReferNivComm', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnft6a11MoisSupplemtEVitA_Routin', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnft12a59MoisSupplemt_VitARoutin', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PptEnft0a59MoisAyantNum_EtatC', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Enfts0a59MoisReçuTraumaAccidt_ViolencNbreTot', models.DecimalField(decimal_places=5, max_digits=10)),
                ('DiarrheRefer_NivComm0a59mois', models.DecimalField(decimal_places=5, max_digits=10)),
                ('SuppltSystematic_VitADEnfts6a59Mois', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnfts6a59MoisSuppl_VitA_Routin', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnft12a59MoisDeparasit_Routin', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NbreCasPneumoni0a59mois', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NbreEnft0a59MoisPrestPneumoniGrav_hypoxiTPTh_NivPSF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NbreEnFt0a59MoisPrestPneumoniGrav_HTPTh_NivPPSM', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NbreEnft0a59MoisPrestPneumoniGrav_SaturatO2NivPPSF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('NbreEnft0a59MoisPrestPneumoniGrav_SatO2NivPPSMa', models.DecimalField(decimal_places=5, max_digits=10)),
                ('PtgEnft0a59MoisPrestPneumoniGrav_SatO2NivPPS', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationEtRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('NomDistrict', models.CharField(max_length=250)),
                ('TxCouver_Penta3', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxCouvert_RR1', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TxCouvert_HepBInfOuEgal2H', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Tot0A11MoisNbreEnftCompletVacc', models.DecimalField(decimal_places=5, max_digits=10)),
                ('RR2Couvert12A23Mois', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Tot12A23MoisFNbreEnftCompletVacc', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Tot12A23MoisMNbreEnftCompletVacc', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Visiteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('date_visiteur', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

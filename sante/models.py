from django.db import models


class PlanificationFamiliale(models.Model):
    CodeDistrict = models.IntegerField()
    NomDistrict = models.CharField(max_length=250)
    TxRecrutementPF = models.DecimalField(max_digits=10, decimal_places=5)
    TxdAbandonPF = models.DecimalField(max_digits=10, decimal_places=5)
    TotAbandonsPF = models.DecimalField(max_digits=10, decimal_places=5)
    PctagF15a49ansSMCapresAvortt = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctageUtilisacPF = models.DecimalField(max_digits=10, decimal_places=5)
    PcetageUtilisatPF_15a49ans = models.DecimalField(
        max_digits=10, decimal_places=5)
    TxPrevalencContraceptv = models.DecimalField(
        max_digits=10, decimal_places=5)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.NomDistrict)


class GouvernanceSante(models.Model):
    CodeDistrict = models.IntegerField()
    NomDistrict = models.CharField(max_length=250)

    DepensFonctment = models.IntegerField()
    DepensInvistisnt = models.IntegerField()
    MassSalarial = models.IntegerField()
    PersMedical = models.IntegerField()
    PersAppui = models.IntegerField()
    MasSalarialPersSanitairAppui = models.IntegerField()
    DepensEauDomainSante = models.IntegerField()
    DepensElectDomainSante = models.IntegerField()
    AchatMedicaAidSocial = models.IntegerField()
    TotDepensSant = models.IntegerField()
    DepensInvestisSant = models.IntegerField()
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.NomDistrict)


class ReproductionEtJeune(models.Model):
    CodeDistrict = models.IntegerField()
    NomDistrict = models.CharField(max_length=250)
    PctagAdo15a19anSousMC_aprAvort = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctagAdo20a24anSousMC_AprAvort = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctagAvortAdo15a19anPEC_AmiuAuPT = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctagAvortF20a24anPEC_AuPTMisoprostol = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctagAvortAdo20a24anPEC_AmiuAuPT = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctagAvortAdo15a19anPEC_AuPTMisoprostol = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctagAccouchAdo15a19an_AssistPerQalifi = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctagAccouchAdo20a24an_AssistPersQalifie = models.DecimalField(
        max_digits=10, decimal_places=5)
    PctagUtilisatc_PF_15a49ans = models.DecimalField(
        max_digits=10, decimal_places=5)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.NomDistrict)


class SanteAlimentationEtNutrition(models.Model):
    CodeDistrict = models.IntegerField()
    NomDistrict = models.CharField(max_length=250)

    PtgEnftDemoins5anAyantInsuffisPonderal1 = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgFEnceintesPresentantAnemie = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnfmoins5anAyantInsuffisPonderal = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftmoin5anAyantInsuffisPonderalModere = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftmoin5ansAyantInsuffisPonderalGrav = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftmoin5anAyanInsuffisPonderalGlobal = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftmoin5anAyantMASsansComplication = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftmoin5anSouffranMAM = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftMoin5anDepistMalnutriAigu = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgFEnceintPresentMalnutriAigu = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftMoins5anPresentAnemi = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftmoin5anAyantRetardCSeverTA = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnftMoin5anAyantRetarCroissancTA = models.DecimalField(
        max_digits=10, decimal_places=5)
    TxAbandonEnftMoin5anMASAuCREN = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnft6a59moisDepistMAM = models.DecimalField(
        max_digits=10, decimal_places=5)
    NvxAdmissionLieRechutCREN = models.DecimalField(
        max_digits=10, decimal_places=5)
    NvxAdmissionLieRechutUREN = models.DecimalField(
        max_digits=10, decimal_places=5)
    TxGuerisonEnft6a59MoisMASaLUREN = models.DecimalField(
        max_digits=10, decimal_places=5)
    TTEnftsMAM6a59MoisDepistes = models.DecimalField(
        max_digits=10, decimal_places=5)
    TxDeGuerisonUREN = models.DecimalField(max_digits=10, decimal_places=5)
    PptEnftMoins5anSouffranMAM = models.DecimalField(
        max_digits=10, decimal_places=5)
    TxDeMASTraitAvecSuccesAuCREN = models.DecimalField(
        max_digits=10, decimal_places=5)
    PptEnftMoins5anAyantInsuffisPS = models.DecimalField(
        max_digits=10, decimal_places=5)
    PptEnftMoins5anMASGueri = models.DecimalField(
        max_digits=10, decimal_places=5)
    MalnutChronic_RetarCSeverTA = models.DecimalField(
        max_digits=10, decimal_places=5)
    MalnutChronicO_RetardCMTA = models.DecimalField(
        max_digits=10, decimal_places=5)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.NomDistrict)


class SantePaludisme (models.Model):
    CodeDistrict = models.IntegerField()
    NomDistrict = models.CharField(max_length=250)

    TxMorbiditPptnellPalustreTTAge = models.DecimalField(
        max_digits=10, decimal_places=5)
    TxMorbiditPptnellPalustreFEnceint = models.DecimalField(
        max_digits=10, decimal_places=5)
    TxmorbiditPptnellePalustrMoins5ans = models.DecimalField(
        max_digits=10, decimal_places=5)
    IncidencPaludism_1000Habts = models.DecimalField(
        max_digits=10, decimal_places=5)
    IncidencPaludismgGravTT = models.DecimalField(
        max_digits=10, decimal_places=5)
    CasPaludismConfirmTT = models.DecimalField(max_digits=10, decimal_places=5)
    NbreTTCasPaluSimplConfirmInsttTRecuTaitemt = models.DecimalField(
        max_digits=10, decimal_places=5)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.NomDistrict)


class SurvieEnfant(models.Model):
    CodeDistrict = models.IntegerField()
    NomDistrict = models.CharField(max_length=250)
    PtgEnft0a59MoisAyantDiarrhe = models.DecimalField(
        max_digits=10, decimal_places=5)
    PptCasPneuMoni0a59Mois = models.DecimalField(
        max_digits=10, decimal_places=5)
    PptEnftPneumoniGravSaturatO2Mesure = models.DecimalField(
        max_digits=10, decimal_places=5)
    PptEnft0a59MoisSouffranAnemi = models.DecimalField(
        max_digits=10, decimal_places=5)
    PptEnft0a59moisPresenttAnemi = models.DecimalField(
        max_digits=10, decimal_places=5)
    CasEnftMoins5ansBSoignCtrDiarrhCentr = models.DecimalField(
        max_digits=10, decimal_places=5)
    NbreCasDiarrhReferNivComm = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnft6a11MoisSupplemtEVitA_Routin = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnft12a59MoisSupplemt_VitARoutin = models.DecimalField(
        max_digits=10, decimal_places=5)

    PptEnft0a59MoisAyantNum_EtatC = models.DecimalField(
        max_digits=10, decimal_places=5)
    Enfts0a59MoisReçuTraumaAccidt_ViolencNbreTot = models.DecimalField(
        max_digits=10, decimal_places=5)
    DiarrheRefer_NivComm0a59mois = models.DecimalField(
        max_digits=10, decimal_places=5)
    SuppltSystematic_VitADEnfts6a59Mois = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnfts6a59MoisSuppl_VitA_Routin = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnft12a59MoisDeparasit_Routin = models.DecimalField(
        max_digits=10, decimal_places=5)
    NbreCasPneumoni0a59mois = models.DecimalField(
        max_digits=10, decimal_places=5)
    NbreEnft0a59MoisPrestPneumoniGrav_hypoxiTPTh_NivPSF = models.DecimalField(
        max_digits=10, decimal_places=5)
    NbreEnFt0a59MoisPrestPneumoniGrav_HTPTh_NivPPSM = models.DecimalField(
        max_digits=10, decimal_places=5)
    NbreEnft0a59MoisPrestPneumoniGrav_SaturatO2NivPPSF = models.DecimalField(
        max_digits=10, decimal_places=5)
    NbreEnft0a59MoisPrestPneumoniGrav_SatO2NivPPSMa = models.DecimalField(
        max_digits=10, decimal_places=5)
    PtgEnft0a59MoisPrestPneumoniGrav_SatO2NivPPS = models.DecimalField(
        max_digits=10, decimal_places=5)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.NomDistrict)


class VaccinationEtRoutine(models.Model):
    CodeDistrict = models.IntegerField()
    NomDistrict = models.CharField(max_length=250)
    TxCouver_Penta3 = models.DecimalField(max_digits=10, decimal_places=5)
    TxCouvert_RR1 = models.DecimalField(max_digits=10, decimal_places=5)
    TxCouvert_HepBInfOuEgal2H = models.DecimalField(
        max_digits=10, decimal_places=5)
    Tot0A11MoisNbreEnftCompletVacc = models.DecimalField(
        max_digits=10, decimal_places=5)
    RR2Couvert12A23Mois = models.DecimalField(max_digits=10, decimal_places=5)
    Tot12A23MoisFNbreEnftCompletVacc = models.DecimalField(
        max_digits=10, decimal_places=5)
    Tot12A23MoisMNbreEnftCompletVacc = models.DecimalField(
        max_digits=10, decimal_places=5)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.NomDistrict)


class Visiteur (models.Model):
    nom = models.CharField(max_length=25)
    date_visiteur = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

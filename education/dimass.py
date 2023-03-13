from django.forms import ModelForm
from education.models import DimEduc_Access
from django import forms


class acc(ModelForm):
    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    PrescoEnsGrcns3et5ans = forms.CharField(label='Ensemble des garçons âgés entre 3 et 5 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEnsFilles3et5ans = forms.CharField(label='Ensemble des filles âgées entre 3 et 5 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEnsFilesEtGrcnsAge3Et5ans = forms.CharField(label='Ensemble des filles et des garçons âgés entre 3 et 5 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectGrcnsInscritsPresco = forms.CharField(label='Effectif des garçons inscrits au prescolaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectFilleInscritPresco = forms.CharField(label='Effectif des filles inscrites au prescolaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectTTInscritPresco = forms.CharField(label='Effectif total des élèves inscrits au prescolaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectPS = forms.CharField(label='Effectifs du préscolaire, petite section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectMS = forms.CharField(label='Effectifs du préscolaire, moyenne section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectGS = forms.CharField(label='Effectifs du préscolaire, grande section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectTotal = forms.CharField(label=' Effectifs du préscolaire, Total ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoNbreGrcnsFillesEnPS = forms.CharField(label='Nombre de garçons (de filles) en petite section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoNbreGrcnsFillesEnMS = forms.CharField(label='Nombre de garçons (de filles) en moyenne section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoNbreGrcnsFillesEnGS = forms.CharField(label='Nombre de garçons (de filles) en grande section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoNbreFillesPrescoTotal = forms.CharField(label='Nombre de filles au prescolaire (Total)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    PrescoEffectTTInscritPreslrePublic = forms.CharField(label='Effectifs total des élèves inscrits au prescolaire dans le public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffecTTElvInscritsPrescoStructComm = forms.CharField(label='Effectifs total des élèves inscrits au prescolaire dans les structures communautaires/associatives', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectTTElvInscritPrecoPrive = forms.CharField(label='Effectifs total des élèves inscrits au prescolaire dans le privé', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectifTTElvFillesInscritPrecoPrive = forms.CharField(label='Effectifs total des élèves inscrits au prescolaire public (filles)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoEffectifTTFillesIncritStructComm = forms.CharField(label='Effectifs total des élèves inscrits au prescolaire dans les structures communautaires/associatives (filles)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    PrescoEffectifTTFillesAuPrescoStructComm = forms.CharField(label='Effectifs total des élèves inscrits au prescolaire dans le privé (filles)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoNbreTTNvxInscritsPS = forms.CharField(label='Nombre total de nouveaux inscrits en petite section quel que soit leur âge', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PrescoNbreTTNvxInscritsMS = forms.CharField(label='Nombre total de nouveaux inscrits en moyenne section quel que soit leur âge', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreTTNvxInscritGS = forms.CharField(label='Nombre total de nouveaux inscrits en grande section quel que soit leur âge', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructurePrescoPublic = forms.CharField(label='Nombre de structures préscolaires du public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructurePrescolairePrive = forms.CharField(label='Nombre de structures préscolaires du privé', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    NbreStructurePrescolaireComm = forms.CharField(label='Nombre de structures préscolaires communautaires', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectlevesPrescolAyantPieceEtatCivilPS = forms.CharField(label='Effectifs délèves du prescolaire nayant pas une pièce détat civil en Petite Section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectElvesPrescolAyantPiecEtatCivilMS = forms.CharField(label='Effectifs délèves du prescolaire nayant pas une pièce détat civil en moyenne section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectPrecolAyantPieceEtatCivilGS = forms.CharField(label='Effectifs délèves du prescolaire nayant pas une pièce détat civil en grande section', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectEnfantsPrescolFrancoArabe = forms.CharField(label='Effectifs des enfants du prescolaire franco-arabe', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    NbreDaaraModerne = forms.CharField(label='Nombre de Daara modernes', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreDaaraMiseAJour = forms.CharField(label='Nombre de Daara mise à niveau', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreGarconsDe6A11ans = forms.CharField(label='Nombre de garçons de la tranche de 6 à 11 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreFillesDe6A11ans = forms.CharField(label='Nombre de filles de la tranche de 6 à 11 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreEnfantsDe6A11ans = forms.CharField(label='Nombre denfants de la tranche de 6 à 11 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ElNbreEleveElmtaire = forms.CharField(label='Nombre délèves dans lélémentaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreGarconsElmtaire = forms.CharField(label='Nombre de garçons dans lélémentaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreFillesElmtaire = forms.CharField(label='Nombre de filles dans lélémentaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectsElmtairePrive = forms.CharField(label='Effectifs de lélémentaire dans le privé', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectsElmtairePublic = forms.CharField(label='Effectifs de lélémentaire dans le public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ElEfectPrimStructComm = forms.CharField(label='Effectifs de lélémentaire dans les structures communautaires', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectsElvesPrimSituationHandicap = forms.CharField(label='Effectifs des élèves en situation de handicap total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectFillesPrimSituationHandicap = forms.CharField(label='Effectifs des élèves en situation de handicap filles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectGarcsPrimSituationHandicap = forms.CharField(label='Effectifs des élèves en situation de handicap Garcons', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEffectifTTElevesElementaire = forms.CharField(label='Effectif total des élèves de lélémentaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ElEfectTTElvesPasPieceEtatCivil = forms.CharField(label='Effectif total des élèves ne disposant pas de pièce détat civil', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectTTElevesCI = forms.CharField(label='Effectif total des élèves de CI', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectlTTElevesCM2 = forms.CharField(label='Effectif total des élèves de CM2', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectEnftsPrimFrancoArabe = forms.CharField(label='Effectifs des enfants de lélémentaire franco-arabe', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectPrimRedoublantsTotal = forms.CharField(label='Effectifs de lélémentaire - redoublants total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ElEfectPrimRedblantsFilles = forms.CharField(label='Effectifs de lélémentaire - redoublants filles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectPrimRedblantGrcons = forms.CharField(label='Effectifs de lélémentaire - redoublants Garcons', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEffectifsCI = forms.CharField(label='Effectifs  CI', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEffectifsCP = forms.CharField(label='Effectifs  CP', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEffectifsCE1 = forms.CharField(label='Effectifs  CE1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ElEffectifsCE2 = forms.CharField(label='Effectifs  CE2', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEffectifsCM1 = forms.CharField(label='Effectifs  CM1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEffectifsCM2 = forms.CharField(label='Effectifs  CM2', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreRedoublantCI = forms.CharField(label='Nombre Redoublants CI', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreRedoublantCP = forms.CharField(label='Nombre Redoublants  CP', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ElNbreRedoublantsCE1 = forms.CharField(label='Nombre Redoublants  CE1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreRedoublantsCE2 = forms.CharField(label='Nombre Redoublants  CE2', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreRedoublantsCM1 = forms.CharField(label='Nombre Redoublants  CM1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreRedoublantsCM2 = forms.CharField(label='Nombre Redoublants  CM2', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectTotalInscritElmtaire = forms.CharField(label='Effectif total inscrit à lélémentaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectGrconsInscritElmtaire = forms.CharField(label='Effectif garçons inscrits à lélémentaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElEfectFillesIncritElmtaire = forms.CharField(label='Effectif filles inscrites à lélémentaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreElvesSituationHandicap = forms.CharField(label='Nombre délèves en situation dhandicap', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreTleElevesElmtaire = forms.CharField(label='Nombre total délèves à lélémentaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElPopOfciellemntScolarbleJnes6_11ans = forms.CharField(label='Population officiellement scolarisable à lélémentaire (population des jeunes de la tranche 6-11 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElPopOficielemntScolarbleGrcons6_11ans = forms.CharField(label='Population des garçons officiellement scolarisable à lélémentaire (population des jeunes de la tranche 6-11 ans )', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElPopOficielemntScolarbleFilles6_11ans = forms.CharField(label='Population des filles officiellement scolarisable à lélémentaire(population des jeunes de la tranche 6-11 ans)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreElvesQuittEtablisPourHorsComm = forms.CharField(label='Nombre délèves quittant un établissement de la commune pour un autre se sitant hors de la commune', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreElvesProvncEtablisSituantAutrComm = forms.CharField(label='Nombre délèves en provenance dun établissement se situant dans une autre commune', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreEcolElmntairePublic = forms.CharField(label='Nombre décoles élémentaires publiques', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElNbreEcolElmntairePrive = forms.CharField(label='Nombre décoles élémentaires privées', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MGEnsbleGrconsEntre12Et15ans = forms.CharField(label='Ensemble des garçons âgés entre 12 et 15 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MGEnsFillesEntre12Et15ans = forms.CharField(label='Ensemble des filles âgées entre 12 et 15 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MGNbreElvesMG = forms.CharField(label='Nombre délèves Moyen Général', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MGNbreElvesFilles = forms.CharField(label='Nombre délèves Filles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MGNbreElvesGrcons = forms.CharField(label='Nombre délèves Garcons', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MGEfectsMGPublic = forms.CharField(label='Effectifs du moyen général public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MGEfectifMGPrive = forms.CharField(label='Effectifs du moyen général privé', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MGRedblantsTotal = forms.CharField(label='Redoublants total moyen général', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    RedblantsFillesMG = forms.CharField(label='Redoublants filles moyen général', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    RedblantsGrconsMG = forms.CharField(label='Redoublants Garcons moyen général', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectsInscritMGFrancoArabe = forms.CharField(label='Effectifs inscrits au moyen général franco-arabe', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EffectifsMG6eme = forms.CharField(label='effectifs du moyen général 6e', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EffectifsMG5eme = forms.CharField(label='effectifs du moyen général 5e', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EffectifMG4e = forms.CharField(label='effectifs du moyen général 4e', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EffectifMG3e = forms.CharField(label='effectifs du moyen général 3e', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublants6e = forms.CharField(label='Nombre de redoublants 6e', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublants5e = forms.CharField(label='Nombre de redoublants 5e', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublants4e = forms.CharField(label='Nombre de redoublants 4e', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublants3e = forms.CharField(label='Nombre de redoublants 3e', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectTotalIncritMG = forms.CharField(label='Effectif total inscrit au moyen général', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PopJeunesTranche12_15ans = forms.CharField(label='Population officiellement scolarisable à lélémentaire (population des jeunes de la tranche 12-15 ans )', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevsEfectivmntInscrit6em1erFs = forms.CharField(label='Nombre délèves effectivement inscrits en 6e pour la première fois, sans distinction dâge', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNouvxInscritFilles6eme = forms.CharField(label='Nombre de nouveaux inscrits-filles en 6em', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreTotlNouvxInscrit6eme = forms.CharField(label='Nombre total de nouveaux inscrits en 6em', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNouvxInscrit6emePublic = forms.CharField(label='Nombre de nouveaux inscrits en 6e dans les établissements publics', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvSituationHandicapMG = forms.CharField(label='Nombre délèves en situation dhandicap', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreTotElvMoyGenral = forms.CharField(label='Nombre total délèves MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvesMarieCrsAnnMG = forms.CharField(label='Nombre délèves filles mariées en cours dannée', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvFillesVictimGrosseMG = forms.CharField(label='Nombre délèves filles victimes de grosses durant lannée', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreFilleVictimViolencSexuelMG = forms.CharField(label='Nombres Filles victimes de violences sexuelles par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrconsVictimViolencSexuelMG = forms.CharField(label='Nombres Garcons victimes de violences sexuelles par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreFillesOrphelinMG = forms.CharField(label='Nombre Filles orphelins par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreTotFilleMG = forms.CharField(label='Nombre total de fille au Moyen General', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrconsOrphelinMG = forms.CharField(label='Nombre Garcons orphelins par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    GrconsAge16_18ans = forms.CharField(label='Ensemble des garçons âgés entre 16 et 18 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    FillesAge16_18ans = forms.CharField(label='Ensemble des filles âgées entre 16 et 18 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsFillesGrconsAge16_18ans = forms.CharField(label='Ensemble des filles et des garçons âgés entre 16 et 18 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvScdaire = forms.CharField(label='nombre délève dans le secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrconsScdaire = forms.CharField(label='nombre de garçons dans le secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreFillesScdaire = forms.CharField(label='nombre de filles dans le secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectScdairePublic = forms.CharField(label='Effectifs du secondaire public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectScdairePrive = forms.CharField(label='Effectifs du secondaire prive', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectScdaireCommun = forms.CharField(label='Effectifs du secondaire communautaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    RedblantsTotScdaireGnral = forms.CharField(label='Redoublants total secondaire général', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    RedblantsFillesScdaireGnral = forms.CharField(label='Redoublants filles secondaire général', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    RedblantsGrconScdaire = forms.CharField(label='Redoublants Garcons secondaire général', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    Effectifs2nd = forms.CharField(label='effectifs 2nd', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    Effectifs1er = forms.CharField(label='effectifs 1er', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EffectifsTle = forms.CharField(label='effectifs Terminale', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedblants2nd = forms.CharField(label='Nombre de redoublants en 2nd', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedblants1er = forms.CharField(label='Nombre de redoublants en 1er', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedblantsTle = forms.CharField(label='Nombre de redoublants en Terminale', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EfectTotInscritScdaire = forms.CharField(label='Effectif total inscrit au secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PopJeunesTranch16_18ans = forms.CharField(label='Population officiellement scolarisable au secondaire (population des jeunes de la tranche 16-18 ans )', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvSituationHandicapScnd = forms.CharField(label='Nombre délèves en situation dhandicap ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreTotElvesSecndaire = forms.CharField(label='Nombre total délèves au secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreFilleMarieEnCourAnScdaire = forms.CharField(label='Nombre délèves filles mariées en cours dannée', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvFilleVictimGrosessScndre = forms.CharField(label='Nombre délèves filles victimes de grosses durant lannée ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvsVictimViolencSexuelEtablis = forms.CharField(label='Nombres délèves victimes de violences sexuelles par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreFilleVictimViolencSexuelScdre = forms.CharField(label='Nombres filles victimes de violences sexuelles par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrconVictimViolencSexuelScdair = forms.CharField(label='Nombres garcons victimes de violences sexuelles par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvsOrphelinScndaire = forms.CharField(label='Nombre délèves orphelins établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreFilleOrphelinScndaire = forms.CharField(label='Nombre Filles orphelins par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrconsOrphelinScndaire = forms.CharField(label='Nombre Garcons orphelins par établissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvSanPieceEtatCivilScndaire = forms.CharField(label='Nombre délèves nayant pas une pièce détat civil', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Access
        fields = "__all__"

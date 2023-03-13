from django.forms import ModelForm
from education.models import DimEduc_Equipements
from django import forms


class equi(ModelForm):
    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreCasesDesTtPetits = forms.CharField(label='Nombre de cases des tout-petit', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGarderie = forms.CharField(label='Nombre de garderie', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreMaternelle = forms.CharField(label='Nombre de maternelle', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePrescoTt = forms.CharField(label='Nombre de Prescolaire Total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructPrescoDisposantCantinSclre = forms.CharField(label='Nombre de structures préscolaires disposant de cantines scolaires ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSCLocalNormalPresco = forms.CharField(label='ombre de salles de classe avec un local normal', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSCSituationAbrisProvsrPresco = forms.CharField(label='Nombre de salles de classe en situation d abris provisoire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSallesTtPresco = forms.CharField(label='Nombre de salles total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructPrescoAyantClotur = forms.CharField(label='Nombre de structures préscolaires disposant de cloture', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructPrescoAyantElectricit = forms.CharField(label='Nombre de structures préscolaires disposant délectricité', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreToTLatrinFonctionel = forms.CharField(label='Nombre Total de latrines fonctionnelles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LatrinFonctionelGrcons = forms.CharField(label='Latrines fonctionnelles / Garçon', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LatrinFonctionnelFilles = forms.CharField(label='Latrines fonctionnelles / Fille', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePlacesAssises = forms.CharField(label='Nombre de places assises', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevPresco = forms.CharField(label='nombre d élèves presco', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePontEauCournt = forms.CharField(label='Nombre de points d eau courante', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEnftBeneficDeparasitgMTN = forms.CharField(label='Nombre d enfants ayant bénéficiés de déparasitage MTN', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEnftBeneficieDeparasitgFER = forms.CharField(label='Nombre d enfants ayant bénéficiés de déparasitage FER', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructElmntaireAyantCantinScolair = forms.CharField(label='Nombre de structures  disposant de cantines scolaires', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSCPrimAvecLocalNormal = forms.CharField(label='Nombre de salles de classe avec un local normal', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSCPrimSituationAbriProvisoir = forms.CharField(label='Nombre de salles de classe en situation d abris provisoire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSallesTTPrim = forms.CharField(label='Nombre de salles total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructurAyantCloturPrim = forms.CharField(label='Nombre de structures de lélémentaire disposant de cloture', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TTLatrineFonctionnelPrim = forms.CharField(label='Total latrines fonctionnelles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LatrinFonctionnelGrconsPrim = forms.CharField(label='Latrines fonctionnelles / Garçon', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LatrinsFonctionnelFilles = forms.CharField(label='Latrines fonctionnelles / Fille', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolPublicAyantElectricite = forms.CharField(label='Nombre décoles publiques ayant de l éléctricité', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEauCourantePrim = forms.CharField(label='Nombre de points d eau courante', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePlacAssisStructurPublic = forms.CharField(label='Nombre de places assises dans les structures publiques', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePlacAssisStructurPrive = forms.CharField(label='Nombre de places assises dans les structures privées', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvStructurPublicPrimair = forms.CharField(label='Nombre d élèves dans les structures publiques', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvStructurPublicPrive = forms.CharField(label='Nombre d élèves dans les structures privées', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleClassAvecLocalNormal = forms.CharField(label='Nombre de salles de classe avec un local normal:Etablissement primaire public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleClassPrimrSituatAbriProvisoir = forms.CharField(label='Nombre de salles de classe en situation dabris provisoire(Etablissement primaire public)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleTotEtablisPrimPublic = forms.CharField(label='Nombre de salles total(Etablissement primaire public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrpPedagogicPrim = forms.CharField(label='Nombre de groupes pédagogiques ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreClassePhysicPrim = forms.CharField(label='Nombre de classes physiques', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolEquipeSalleITPrim = forms.CharField(label='Nombre d écoles équipées en salle informatique', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolPrimAyantConexionNet = forms.CharField(label='Nombre d écoles disposant d une connexion internet', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructreAyantCatinScolreMG = forms.CharField(label='Nombre de structures  disposant de cantines scolaires', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleClassAcLocalNormalMG = forms.CharField(label='Nombre de salles de classe avec un local normal', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleClassSituatAbriProvisoirMG = forms.CharField(label='Nombre de salles de classe en situation d abris provisoire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleTotalMG = forms.CharField(label='Nombre de salles total moyen general', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructurElmntreAyantCloturMG = forms.CharField(label='Nombre de structures de lélémentaire disposant de cloture MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TotLatrinFonctionnelMG = forms.CharField(label='Total latrines fonctionnelles MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LatrinFonctionnelGrconsMG = forms.CharField(label='Latrines fonctionnelles / Garçon MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LatrinFonctionnelFilleMG = forms.CharField(label='Latrines fonctionnelles / Fille MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolPublicAyantElectMG = forms.CharField(label='Nombre décoles publiques ayant de l éléctricité MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEauCouranteMG = forms.CharField(label='Nombre de points deau courante', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePlaceAssisStructurPublicMG = forms.CharField(label='Nombre de places assises dans les structures publiques MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePlacAssiseStructurPrivMG = forms.CharField(label='Nombre de places assises dans les structures privées MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvStructurPublicMG = forms.CharField(label='Nombre délèves dans les structures publiques MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevStructurPrivMG = forms.CharField(label='Nombre délèves dans les structures privées MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleClassAvcLocalNormalMG = forms.CharField(label='Nombre de salles de classe avec un local normal(Etablissement primaire public)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrpPedagogicMG = forms.CharField(label='Nombre de groupes pédagogiques', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreClassPhysicMG = forms.CharField(label='Nombre de classes physiques', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolEquipSalleTIMG = forms.CharField(label='Nombre d écoles équipées en salle informatique MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolAyantConnexionInetMG = forms.CharField(label='Nombre d écoles disposant dune connexion internet MG', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructurAyantCatinScolreSe = forms.CharField(label='Nombre de structures  disposant de cantines scolaires secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleClassAvecLocalNormalSecd = forms.CharField(label='Nombre de salles de classe avec un local normal secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleClassSituatAbriProvisScndre = forms.CharField(label='Nombre de salles de classe en situation dabris provisoire secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSallesTTSecondaire = forms.CharField(label='Nombre de salles total secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructurScndrAyantClotur = forms.CharField(label='Nombre de structures de lélémentaire disposant de cloture secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TTLatrinFonctionnelScndr = forms.CharField(label='Total latrines fonctionnelles secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LatrinGrconFonctionelScndr = forms.CharField(label='Latrines fonctionnelles / Garçon du secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    LatrinFillesFonctionelScndr = forms.CharField(label='Latrines fonctionnelles / Fille du secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolPublicAyantElectScndr = forms.CharField(label='Nombre d écoles publiques ayant de léléctricité du secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEauCourantScndr = forms.CharField(label='Nombre de points deau courante du secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePlacAssisStructPublicScndr = forms.CharField(label='Nombre de places assises dans les structures publiques secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbrePlacAssisStructPrivScndr = forms.CharField(label='Nombre de places assises dans les structures privées secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvStructPublicScndr = forms.CharField(label='Nombre délèves dans les structures publiques secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvStructPrivScndr = forms.CharField(label='Nombre délèves dans les structures privées', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleDeClassAvcLocalNormalScndr = forms.CharField(label='Nombre de salles de classe avec un local normal(Etablissement primaire public)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreSalleTTScndrPublic = forms.CharField(label='Nombre de salles total(Etablissement secondaire public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrpPedagogicScndr = forms.CharField(label='Nombre de groupes pédagogiques secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreClassPhysicScndr = forms.CharField(label='Nombre de classes physiques secondaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolEquipSalleITScndr = forms.CharField(label='Nombre décoles équipées en salle informatique', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEcolAyantConexionNetScndr = forms.CharField(label='Nombre décoles disposant dune connexion internet', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:

        model = DimEduc_Equipements
        fields = "__all__"

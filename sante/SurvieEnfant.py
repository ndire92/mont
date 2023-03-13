from django.forms import ModelForm
from sante.models import SurvieEnfant
from django import forms


class survienf(ModelForm):
    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PtgEnft0a59MoisAyantDiarrhe = forms.DecimalField(label='Pourcentage denfants 0- 59 mois ayant fait une diarrhée', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PptCasPneuMoni0a59Mois = forms.DecimalField(label='R20_Proportion de cas de pneumonie 0-59 mois', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PptEnftPneumoniGravSaturatO2Mesure = forms.DecimalField(label='R20_Proportion denfants avec pneumonie grave dont la saturation en oxygène a été mesurée', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PptEnft0a59MoisSouffranAnemi = forms.DecimalField(label='R20_Proportion denfants de 0-59 mois souffrant danémie', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PptEnft0a59moisPresenttAnemi = forms.DecimalField(label='R20_Proportion d’enfants de 0 -59 mois présentant une anémie', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    CasEnftMoins5ansBSoignCtrDiarrhCentr = forms.DecimalField(label='SAVE-% de cas denfants de moins de 5 ans correctement soignés contre la diarrhée dans les centres de santé communautaires', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    NbreCasDiarrhReferNivComm = forms.DecimalField(label='Nombre de cas de diarrhee referes par le niveau communautaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PtgEnft6a11MoisSupplemtEVitA_Routin = forms.DecimalField(label='R20_Pourcentage denfants  de 6 -11 mois supplémentés en vitamine A en routine', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PtgEnft12a59MoisSupplemt_VitARoutin = forms.DecimalField(label='R20_Pourcentage denfants de 12 -59 mois supplémentés en vitamine A en routine', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PtgEnft12a59MoisDeParasit_Routin = forms.DecimalField(label='R20_Pourcentage denfants de 12- 59 mois déparasités en routine', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))	
    PptEnft0a59MoisAyantNum_EtatC = forms.DecimalField(label='R20_Proportion denfants de 0 - 59 mois ayant un numéro détat civil', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    Enfts0a59MoisReçuTraumaAccidt_ViolencNbreTot = forms.DecimalField(label='R20_Enfants de 0-59 mois reçus pour traumatisme dus à un accident et/ou à un acte de violence / Nombre total denfants 0 - 59 mois vus en consultation', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    DiarrheRefer_NivComm0a59mois = forms.DecimalField(label='Diarrhée référés par le niveau communautaire (0-59 mois)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    SuppltSystematic_VitADEnfts6a59Mois = forms.DecimalField(label='Supplémentation systématique en vitamine A des enfants de 6 à 59 mois', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PtgEnfts6a59MoisSuppl_VitA_Routin = forms.DecimalField(label='R20_Pourcentage denfants de 6 -59 mois supplémentés en vitamine A en routine', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PtgEnft12a59MoisDeparasit_Routin = forms.DecimalField(label='Pourcentage enfants 12- 59 mois déparasités en routine OK', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    NbreCasPneumoni0a59mois = forms.DecimalField(label='R20_Nombre de cas de pneumonies 0 – 59 mois', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    NbreEnft0a59MoisPrestPneumoniGrav_hypoxiTPTh_NivPSF = forms.DecimalField(label='R20_Nombre d’enfants de 0 -59 mois présentant une pneumonie grave avec hypoxie traitée par oxygénothérapie au niveau des PPS Feminin', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    NbreEnFt0a59MoisPrestPneumoniGrav_HTPTh_NivPPSM = forms.DecimalField(label='R20_Nombre d’enfants de 0 -59 mois présentant une pneumonie grave avec hypoxie traitée par oxygénothérapie au niveau des PPS Masculin', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    NbreEnft0a59MoisPrestPneumoniGrav_SaturatO2NivPPSF = forms.DecimalField(label='R20_Nombre d’enfants de 0 -59 mois présentant une pneumonie grave chez qui la saturation en oxygène a été mesurée au niveau des PPS Feminin', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    NbreEnft0a59MoisPrestPneumoniGrav_SatO2NivPPSMa = forms.DecimalField(label='R20_Nombre d’enfants de 0 -59 mois présentant une pneumonie grave chez qui la saturation en oxygène a été mesurée au niveau des PPS Masculin', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PtgEnft0a59MoisPrestPneumoniGrav_SatO2NivPPS = forms.DecimalField(label='R20_Pourcentage d’enfants de 0 -59 mois présentant une pneumonie grave chez qui la saturation en oxygène a été mesurée au niveau des PPS', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    date = forms.CharField(label='Date ajout', widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(label='Date Modification', widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = SurvieEnfant
        fields = "__all__"

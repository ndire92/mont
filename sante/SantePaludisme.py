from django.forms import ModelForm
from sante.models import SantePaludisme
from django import forms


class santePalu(ModelForm):
    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))

    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    TxMorbiditPptnellPalustreTTAge = forms.DecimalField(label='Taux de morbidité proportionnelle palustre:Tous Age', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    TxMorbiditPptnellPalustreFEnceint = forms.DecimalField(label='Taux de morbidité proportionnelle palustre/chez les Femmes enceintes', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    TxmorbiditPptnellePalustrMoins5ans = forms.DecimalField(label='Taux de morbidité proportionnelle palustre/chez les moins de 5 ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    IncidencPaludism_1000Habts = forms.DecimalField(label='IND20_Incidence du paludisme pour 1000 habitants', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    IncidencPaludismgGravTT = forms.DecimalField(label='Incidence du paludisme grave Total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    CasPaludismConfirmTT = forms.DecimalField(label='Cas paludisme confirmés Total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    NbreTTCasPaluSimplConfirmInsttTRecuTaitemt = forms.DecimalField(label='Nombre total de cas paludisme simple confirmés enregistrés sur la période par les DSDOM qui ont reçu un traitement antipaludique approprié, conformément à la politique nationale à travers la PECADOM', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    date = forms.CharField(label='Date Ajout', widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(label='Date de modification', widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = SantePaludisme
        fields = "__all__"

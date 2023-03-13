from django.forms import ModelForm
from sante.models import PlanificationFamiliale
from django import forms


class PLANFF(ModelForm):
    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    TxRecrutementPF = forms.DecimalField(label='Taux Recrutement PF', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    TxdAbandonPF = forms.DecimalField(label='Taux Abadons PF', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    TotAbandonsPF = forms.DecimalField(label='Total  Abadons PF', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PctagF15a49ansSMCapresAvortt = forms.DecimalField(label='R20_Pourcentage de femmes de 15-49 ans sous méthode contraceptive après avortement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PctageUtilisacPF = forms.DecimalField(label='R20_Pourcentage dutilisatrices PF', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    PcetageUtilisatPF_15a49ans = forms.DecimalField(label='R20_Pourcentage dutilisatrices PF chez  les adolescentes de 15-19ans', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    TxPrevalencContraceptv = forms.DecimalField(label='R20_Taux de Prévalence contraceptive', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    date = forms.CharField(label='Date Ajout', widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(label='Date de modification', widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = PlanificationFamiliale
        fields = "__all__"

from django.forms import ModelForm
from education.models import DimEduc_Gouvernance
from django import forms


class Dg(ModelForm):
    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensFonctionnt = forms.CharField(label='Depense Fonctionnaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensInvestis = forms.CharField(label='Dépenses dinvestissement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MassSalarial = forms.CharField(label='Masse Salariale', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PersonelAppui = forms.CharField(label='Personnel dappui', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MassSalarialPersnlCharg = forms.CharField(label='Masse salariale du personnel en charge', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepenseEnEau = forms.CharField(label='Dépense en eau', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensElect = forms.CharField(label='Dépense en électricité', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    AchatFournitScolreAidSocial = forms.CharField(label='Achat de fourniture scolaires et aide sociale', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    BeneficActivRenforcmntCapacitFP = forms.CharField(label='Bénéficiaires des activités de renforcement de capacité et formation professionnel', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensRenforcmntCapacitFP = forms.CharField(label='Dépenses pour le renforcement de capacité et la formation professionnelle', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensHebergtEtudts = forms.CharField(label='Dépenses pour lhébergement des étudiants', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRecompense = forms.CharField(label='Nombre récompenses', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreBours = forms.CharField(label='Nombre de bourses', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MontanRecompens = forms.CharField(label='Montant des récompenses', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MontanBourc = forms.CharField(label='Montant des bouses', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TotDepensEducat = forms.CharField(label='Total des dépenses en éducation / dépenses de fonctionnement', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensInvestismtEducat = forms.CharField(label='Dépenses dinvestissement dans léducation', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensInvestismtEducat = forms.CharField(label='Dépenses dinvestissement dans léducation', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MassSalarialFloat = forms.DecimalField(label='MasseSalarialeDuPersonnelEnChageFloat', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MassSalarialPerslChargFT = forms.DecimalField(label='Masse Salariale Du Personnel En Charge', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    AchaFournitScolairASF = forms.DecimalField(label='Achat Fournit Scolaire ASF', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensRenforcCapacitFPF = forms.DecimalField(label='Depense Renforcement Capacite FPF', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    DepensHebergEtudtsFlt = forms.DecimalField(label='Depense Hebergement Etudts Float', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MontanRecompensFlt = forms.DecimalField(label='Montant Recompense Float ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    MontanBourceFlt = forms.DecimalField(label='Montant Bource Float', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    TotDepensEducatFlt = forms.DecimalField(label='Total Des Depenses En Education Float', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Gouvernance
        fields = "__all__"

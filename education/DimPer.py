from django.forms import ModelForm
from education.models import DimEduc_Perfomance
from django import forms


class DPRF(ModelForm):
    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    NbreNvxInscriCPAnT = forms.CharField(label='Nombre de nouveaux inscrits au CP de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublanCPAnT = forms.CharField(label='Nombre de redoublants au CP de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevesCiAnneeT_1 = forms.CharField(label='Nombre délèves CI de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscriCE1AnT = forms.CharField(label='Nombre de nouveaux inscrits au CE1 de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscriCE2AnT = forms.CharField(label='Nombre de nouveaux inscrits au CE2 de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscriCM1AnT = forms.CharField(label='Nombre de nouveaux inscrits au CM1 de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscriCM2AnT = forms.CharField(label='Nombre de nouveaux inscrits au CM2 de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublanCE1AnT = forms.CharField(label='Nombre de redoublants au CE1 de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublanCE2AnT = forms.CharField(label='Nombre de redoublants au CE2 de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublanCM1AnT = forms.CharField(label='Nombre de redoublants au CM1 de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublanCM2AnT = forms.CharField(label='Nombre de redoublants au CM2 de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevCpAnT_1 = forms.CharField(label='Nombre délèves CP de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevCE1AnT_1 = forms.CharField(label='Nombre délèves CE1 de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevCE2AnT_1 = forms.CharField(label='Nombre délèves CE2 de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevCM1AnT_1 = forms.CharField(label='Nombre délèves CM1 de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElevCM2AnT_1 = forms.CharField(label='Nombre délèves CM2 de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscri5emAnT = forms.CharField(label='Nombre de nouveaux inscrits en 5e de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscri4emAnT = forms.CharField(label='Nombre de nouveaux inscrits en 4e de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscri3emAnT = forms.CharField(label='Nombre de nouveaux inscrits en 3e de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscri1erAnT = forms.CharField(label='Nombre de nouveaux inscrits en 1ère de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscriTleAnT = forms.CharField(label='Nombre de nouveaux inscrits en Terminale de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublan5emAnT = forms.CharField(label='Nombre de redoublants en 5e de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublan4emAnT = forms.CharField(label='Nombre de redoublants en 4e de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublan3emAnT = forms.CharField(label='Nombre de redoublants en 3e de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublan1erAnT = forms.CharField(label='Nombre de redoublants en 1ère de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreRedoublanTleAnT = forms.CharField(label='Nombre de redoublants en Terminale de lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvs6emAnT_1 = forms.CharField(label='Nombre délèves de 6ème de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElvs5emAnT_1 = forms.CharField(label='Nombre élèves de 5ème de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    Nbre4emAnT_1 = forms.CharField(label='Nombre d élèves de 4ème de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    Nbre2ndeAnT_1 = forms.CharField(label='Nombre d élèves de 2nde de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreElev1erAnT_1 = forms.CharField(label='Nombre d élèves de 1ère de lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscriGrconCM2AnT = forms.CharField(label='Nombre de nouveaux inscrits en CM2 à l année t - garçons', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscriFilleCM2AnT = forms.CharField(label='Nombre de nouveaux inscrits en CM2 à lannée t - filles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PopJeunAge11ansAnT = forms.CharField(label='Population des jeunes agés de 11 ans à l année t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscri3emGrconAnT = forms.CharField(label='Nombre de nouveaux inscrits en 3e à l année t (garçons)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscri3emFilleAnT = forms.CharField(label='Nombre de nouveaux inscrits en 3e à l année t (filles) ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PopJeunAge15ansAnT = forms.CharField(label='Population des jeunes agés de 15 ans à l année t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NvxInscri6eme = forms.CharField(label='Nouveaux inscrits en 6ème ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NvxFilleInscri6em = forms.CharField(label='Nouveaux  filles inscrits en 6ème', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NvxGrconInscri6em = forms.CharField(label='Nouveaux  Garcons inscrits en 6ème', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EffectTTInscriCm2AnT_1 = forms.CharField(label='Effectif total inscrit en CM2 à l année t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NvxInscri2ndAnT = forms.CharField(label='Nouveaux inscrits en 2nd à lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NvxGrconInscri2nd = forms.CharField(label='Nouveaux garcons inscrits en 2nd', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NvxFilleInscri2nd = forms.CharField(label='Nouveaux filles inscrits en 2nd', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    efectifTTInscrit3emAnT_1 = forms.CharField(label='Effectif total inscrit en 3e à lannée t-1', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreNvxInscriTleAnT = forms.CharField(label='Nombre de nouveaux inscrits en terminale à lannée t (total)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreFilleNvxInscriTle = forms.CharField(label='Nombre de filles nouveaux inscrits en terminale ', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreGrconNvxInscriTle = forms.CharField(label='Nombre de garcons nouveaux inscrits en terminale', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PopJeunAge18ansAnT = forms.CharField(label='Population des jeunes agés de 18 ans à lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PopJeunGrçsAge18ansAnT = forms.CharField(label='Population des jeunes garçons agés de 18 ans à lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PopJeunFille18ansAnT = forms.CharField(label='Population des jeunes filles agées de 18 ans à lannée t', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatCFEE = forms.CharField(label='Résultats CFEE', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatCFEE_F = forms.CharField(label='Résultats CFEE-Filles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatCFEE_G = forms.CharField(label='Résultats CFEE-Garçons', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatBFEM = forms.CharField(label='Résultats BFEM', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatBFEM_F = forms.CharField(label='Résultats BFEM-Filles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatBfem_G = forms.CharField(label='Résultats BFEM-Garçons', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatBac = forms.CharField(label='Résultats BAC', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatBac_F = forms.CharField(label='Résultats BAC-Filles', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ResultatBac_G = forms.CharField(label='Résultats BAC-Garçons', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Perfomance

        fields = "__all__"

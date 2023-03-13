from django.forms import ModelForm
from education.models import DimEduc_Personnel
from django import forms


class DPR(ModelForm):
    CodeDistrict = forms.CharField(label='Code District', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NomDistrict = forms.CharField(label='Nom District', widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    EnseigtPrescoPublic = forms.CharField(label='Enseignants au prescolaire pulic', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPrescoPrive = forms.CharField(label='Enseignants au prescolaire privé', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPrescoComm = forms.CharField(label='Enseignants au prescolaire com/ass', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPrescoTot = forms.CharField(label='Enseignants au prescolaire total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElvsPrescoPublic = forms.CharField(label='Elèves au prescolaire public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElvsPrescoPrive = forms.CharField(label='Elèves au prescolaire privé', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElvsPrescoComm = forms.CharField(label='Elèves au prescolaire communautaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElvsPrescoTT = forms.CharField(label='Elèves au prescolaire total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreStructPrescoAyantInfirm = forms.CharField(label='Nombre de structures disposant au moins dun infirmier scolaire dune infirmerie', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPrimPublic = forms.CharField(label='Enseignants au primaire public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPrimPrive = forms.CharField(label='Enseignants au primaire privé', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPrimComm = forms.CharField(label='Enseignants au primaire communautaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPrimTT = forms.CharField(label='Enseignants au primaire Total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElvsPrimPublic = forms.CharField(label='Elèves au primaire public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElvsPrimPrive = forms.CharField(label='Elèves au primaire privé', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElvsPrimComm = forms.CharField(label='Elèves au primaire communautaire', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreClass1MtreDonneCrscohortPrim = forms.CharField(label='Nombre de classes dans lesquelles un seul maître donne cours à deux cohortes d élèves (A et B) en alternance', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreClass1EnseiChargPlsrsNVPrim = forms.CharField(label='Nombre de classes dans lesquelles un seul enseignant est chargé simultanément de plusieurs niveaux', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEclPPubliAyanAMInfirmiSco = forms.CharField(label='Nombre décoles primaires publiques disposant au moins dun infirmier scolaire dune infirmerie', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEclPPrivAyantAMInfirmSco = forms.CharField(label='Nombre d écoles primaires privées disposant au moins d un infirmier scolaire d une infirmerie', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEclPCommAyantAMInfirmSco = forms.CharField(label='Nombre décoles primaires communautaires disposant au moins d un infirmier scolaire d une infirmerie', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPAyantDP_PCAP = forms.CharField(label='enseignants du primaire  ayant diplôme professionnel CAP', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigPAyantD_CEAP = forms.CharField(label='enseignants du primaire  ayant diplôme professionnel CEAP', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPSans_DP = forms.CharField(label='enseignants du primaire  sans diplôme professionnel', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPAyant_Bac = forms.CharField(label='enseignants du primaire ayant le diplôme académique BAC', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPAyant_BFEM = forms.CharField(label='enseignants du primaire ayant le diplôme académique Bfem', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPAyant_CFEE = forms.CharField(label='enseignants du primaire ayant le diplôme académique CFEE', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPAyant_BacPs2 = forms.CharField(label='enseignants du primaire ayant le diplôme académique Bac+2', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPAyant_Licenc = forms.CharField(label='enseignants du primaire ayant le diplôme académique licence', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPAyant_DM_DM_DEA = forms.CharField(label='enseignants du primaire ayant le diplôme académique Maîtrise/Master/DEA', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtPAyantAutre_D = forms.CharField(label='enseignants du primaire ayant  Autres diplôme académique', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEnseigt6emA3em = forms.CharField(label='Nombre denseignants  (6ème à 3ème)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEnseigtH6emA3em = forms.CharField(label='Nombre denseignants hommes (6ème à 3ème)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEnseigtF6emeA3eme = forms.CharField(label='Nombre denseignants femmes (6ème à 3ème)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPcMGSelon_DProCAECEM = forms.CharField(label='des enseignants du public (collège) selon le diplôme professionnel CAECEM', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPublicColleg_DProCAES = forms.CharField(label='des enseignants du public (collège) selon le diplôme professionnel CAES', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPublicCollegSans_DPro = forms.CharField(label='des enseignants du public (collège) sans diplôme professionnel', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElevTotMG6emA3em = forms.CharField(label='Elèves total au moyen général (6ème à 3ème)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElevGrconMG6A3em = forms.CharField(label='Elèves Garcons au moyen général (6ème à 3ème)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElevFilleMoyG6emA3em = forms.CharField(label='Elèves Filles au moyen général (6ème à 3ème)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PerAdminfMoySecond_H = forms.CharField(label='Personnel administratif moyen secondaire Homme', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PersAdminMoySecond_F = forms.CharField(label='Personnel administratif moyen secondaire Fille', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    PersAdminMoySecondTot = forms.CharField(label='Personnel administratif moyen secondaire total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtLyceePublic = forms.CharField(label='Enseignants au Lycée public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtLyceePrive = forms.CharField(label='Enseignants au Lycée privée', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnseigtTotLyce = forms.CharField(label='Enseignants total au Lycée', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElevTTSecondG_2nd_Tle = forms.CharField(label='Elèves total au secondaire général (2nd à Tle)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElevGrconSecondG_2nd_Tle = forms.CharField(label='Elèves Garcons au secondaire général (2nd à Tle)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    ElevFilleSecondG_2nd_Tle = forms.CharField(label='Elèves Filles au secondaire général (2nd à Tle)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEnseigtTT2nd_Tle = forms.CharField(label='Nombre denseignants total  (2nd à Tle)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEnseigtH_2nd_Tle = forms.CharField(label='Nombre denseignants hommes (2nd à Tle)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreEnseigtFille2nd_Tles = forms.CharField(label='Nombre denseignants Filles (2nd à Tle)', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreMedcinEtablisPulicSecond = forms.CharField(label='Nombre de medecin scolaire détablissement public', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreMedcinEtablisPriveSecond = forms.CharField(label='Nombre de medecin scolaire détablissement privée', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreMedcincondTT = forms.CharField(label='Nombre de medecin scolaire total', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPublicSecondAyan_DAcademiBAC = forms.CharField(label='Enseignants du public ayant le diplôme académique BAC', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPublicSecondAyan_DA_BFEM = forms.CharField(label='Enseignants du public ayant le diplôme académique BFEM', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPublicSecondAyan_DA_CFEE = forms.CharField(label='Enseignants du public ayant le diplôme académique CFEE', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPublicSecondAyant_Baspls2 = forms.CharField(label='Enseignants du public ayant le diplôme académique Bac+2', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPublicSecondAyan_Licenc = forms.CharField(label='Enseignants du public ayant le diplôme académique licence', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPcSecondAyan_DM_DM_Plus = forms.CharField(label='Enseignants du public ayant le diplôme académique Maitrise/Master et +', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    EnsPcSecondAyan_Autr_DA = forms.CharField(label='Enseignants du public ayant  autres diplôme académique', widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Personnel
        fields = "__all__"

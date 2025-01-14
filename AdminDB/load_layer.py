import os
import csv
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from .models import Administration, Contribuable, Culturel, Construction, Eclairage_public, Education, Feux_Signalisation, Hebergement, Jeux_Loisirs, Localites, Marchand, Point_eau, Sante, Site_touristique, Sociale, Telecommunication, Assainissement


administration_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nom': 'Nom',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

assainissement_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nature': 'Nature',
    'autoriser': 'Autoriser',
    'aménager': 'Aménager',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

contribuable_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'propriéta': 'Propriéta',
    'raison_soc': 'Raison_Soc',
    'catégorie': 'Catégorie',
    'cadre': 'Cadre',
    'classe': 'Classe',
    'espac_marc': 'Espac_Marc',
    'nom_march': 'Nom_March',
    'téléphon': 'Téléphon',
    'geom': 'MULTIPOINT',
}

culturel_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nom_infras': 'Nom_Infras',
    'catégorie': 'Catégorie',
    'type_infra': 'Type_Infra',
    'statut': 'Statut',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

construction_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'matériau': 'Matériau',
    'usage': 'Usage',
    'standing': 'Standing',
    'permis_bat': 'Permis_Bat',
    'n°_permis': 'N°_Permis',
    'dat_déliv': 'Dat_Déliv',
    'montant_pa': 'Montant_Pa',
    'geom': 'MULTIPOLYGON',
}

eclairage_public_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'type': 'Type',
    'etat': 'Etat',
    'fonctionne': 'Fonctionne',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

education_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nom_ecole': 'Nom_Ecole',
    'statut': 'Statut',
    'cycle': 'Cycle',
    'type_forma': 'Type_Forma',
    'nbr_classe': 'Nbr_Classe',
    'etat_batim': 'Etat_Batim',
    'date_colle': 'Date_Colle',
    'geom': 'MULTIPOINT',
}

feux_signalisation_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'fonctionne': 'Fonctionne',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

hebergement_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nom': 'Nom',
    'type': 'Type',
    'standing': 'Standing',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

jeux_loisirs_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nom_equipe': 'Nom_Equipe',
    'type_equip': 'Type_Equip',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

localites_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'zone_trava': 'Zone_Trava',
    'superficie': 'Superficie',
    'geom': 'MULTIPOLYGON',
}

marchand_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nom_equipe': 'Nom_Equipe',
    'type_equip': 'Type_Equip',
    'statut': 'Statut',
    'etat': 'Etat',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

point_eau_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'type': 'Type',
    'etat': 'Etat',
    'fonctionne': 'Fonctionne',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

sante_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'type_infra': 'Type_Infra',
    'nom_infras': 'Nom_Infras',
    'statut': 'Statut',
    'catégorie': 'Catégorie',
    'etat_batim': 'Etat_Batim',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

site_touristique_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nom': 'Nom',
    'type': 'Type'
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

sociale_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'type_infra': 'Type_Infra',
    'etat_infra': 'Etat_Infra',
    'statut': 'Statut',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

telecommunication_mapping = {
    'id': 'Id',
    'arrondisse': 'Arrondisse',
    'quartier': 'Quartier',
    'lieu_dit': 'Lieu_dit',
    'zone_trava': 'Zone_Trava',
    'nom_equipe': 'Nom_Equipe',
    'opérateur': 'Opérateur',
    'année_col': 'Année_Col',
    'geom': 'MULTIPOINT',
}

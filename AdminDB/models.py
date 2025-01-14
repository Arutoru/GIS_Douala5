from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import Point
from django.utils import timezone
from django.db.models import Manager as GeoManager
import os

# Create your models here.
class Administration(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Assainissement(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nature = models.CharField(max_length=50)
    autoriser = models.CharField(max_length=15)
    aménager = models.CharField(max_length=15)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Contribuable(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    propriéta = models.CharField(max_length=50)
    raison_soc = models.CharField(max_length=50)
    catégorie = models.CharField(max_length=30)
    cadre = models.CharField(max_length=30)
    classe = models.CharField(max_length=30)
    espac_marc = models.CharField(max_length=15)
    nom_march = models.CharField(max_length=50)
    téléphon = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)

class Culturel(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nom_infras = models.CharField(max_length=50)
    catégorie = models.CharField(max_length=30)
    type_infra = models.CharField(max_length=30)
    statut = models.CharField(max_length=15)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Construction(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    matériau = models.CharField(max_length=30)
    usage = models.CharField(max_length=30)
    standing = models.CharField(max_length=30)
    permis_bat = models.CharField(max_length=15)
    n_permis = models.CharField(max_length=50)
    dat_déliv = models.DateField()
    montant_pa = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)

class Eclairage_public(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    etat = models.CharField(max_length=10)
    fonctionne = models.CharField(max_length=15)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Education(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nom_ecole = models.CharField(max_length=50)
    statut = models.CharField(max_length=10)
    cycle = models.CharField(max_length=30)
    type_forma = models.CharField(max_length=50)
    nbr_classe = models.CharField(max_length=10)
    etat_batim = models.CharField(max_length=10)
    date_colle = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Feux_Signalisation(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    fonctionne = models.CharField(max_length=15)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Hebergement(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    standing = models.CharField(max_length=30)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Jeux_Loisirs(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nom_equipe = models.CharField(max_length=50)
    type_equip = models.CharField(max_length=50)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Localites(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    superficie = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

class Marchand(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nom_equipe = models.CharField(max_length=50)
    type_equip = models.CharField(max_length=30)
    statut = models.CharField(max_length=10)
    etat = models.CharField(max_length=10)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Point_eau(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    etat = models.CharField(max_length=30)
    fonctionne = models.CharField(max_length=15)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Sante(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    type_infra = models.CharField(max_length=50)
    nom_infras = models.CharField(max_length=50)
    statut = models.CharField(max_length=10)
    catégorie = models.CharField(max_length=25)
    etat_batim = models.CharField(max_length=10)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)


class Site_touristique(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Sociale(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    type_infra = models.CharField(max_length=50)
    etat_infra = models.CharField(max_length=10)
    statut = models.CharField(max_length=10)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

class Telecommunication(models.Model):
    id = models.IntegerField(primary_key='True')
    arrondisse = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    lieu_dit = models.CharField(max_length=50)
    zone_trava = models.CharField(max_length=50)
    nom_equipe = models.CharField(max_length=50)
    opérateur = models.CharField(max_length=10)
    année_col = models.DateField()
    geom = models.MultiPointField(srid=4326)

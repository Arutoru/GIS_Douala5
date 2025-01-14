from django.contrib import admin

from .models import Administration, Contribuable, Culturel, Construction, Eclairage_public, Education, Feux_Signalisation, Hebergement, Jeux_Loisirs, Localites, Marchand, Point_eau, Sante, Site_touristique, Sociale, Telecommunication, Assainissement
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

# class IncidenceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location')
#
# admin.site.register(Incidence, IncidenceAdmin)

class AdministrationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom')
admin.site.register(Administration,AdministrationAdmin)

class AssainissementAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nature')
admin.site.register(Assainissement,AssainissementAdmin)

class ContribuableAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'raison_soc')
admin.site.register(Contribuable,ContribuableAdmin)

class CulturelAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom_infras')
admin.site.register(Culturel,CulturelAdmin)

class ConstructionAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'standing')
admin.site.register(Construction,ConstructionAdmin)

class Eclairage_publicAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'type')
admin.site.register(Eclairage_public,Eclairage_publicAdmin)

class EducationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom_ecole', 'type_forma')
admin.site.register(Education,EducationAdmin)

class Feux_SignalisationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'fonctionne')
admin.site.register(Feux_Signalisation,Feux_SignalisationAdmin)

class Jeux_LoisirsAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom_equipe', 'type_equip')
admin.site.register(Jeux_Loisirs,Jeux_LoisirsAdmin)

class LocalitesAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'superficie')
admin.site.register(Localites,LocalitesAdmin)

class HebergementAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom', 'standing')
admin.site.register(Hebergement,HebergementAdmin)

class MarchandAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom_equipe', 'type_equip')
admin.site.register(Marchand,MarchandAdmin)

class Point_eauAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'type', 'etat')
admin.site.register(Point_eau,Point_eauAdmin)

class SanteAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom_infras', 'type_infra')
admin.site.register(Sante,SanteAdmin)

class Site_touristiqueAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom', 'type')
admin.site.register(Site_touristique,Site_touristiqueAdmin)

class SocialeAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'type_infra', 'etat_infra')
admin.site.register(Sociale,SocialeAdmin)

class TelecommunicationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'arrondisse', 'quartier', 'lieu_dit', 'nom_equipe')
admin.site.register(Telecommunication,TelecommunicationAdmin)

from django import forms
from .models import *

#Création d'un formulaire
class MediaForms(forms.Form):
    title = forms.CharField()
    description = forms.CharField()

class Creationlivre(forms.Form):
    name = forms.CharField(required=False)
    auteur = forms.CharField(required=False)
    disponible = forms.BooleanField(required=False)

class Updatelivre(forms.Form):
    name = forms.CharField(required=False)
    auteur = forms.CharField(required=False)

class Creationdvd(forms.Form):
    name = forms.CharField(required=False)
    realisateur = forms.CharField(required=False)
    disponible = forms.BooleanField(required=False)

class Updatedvd(forms.Form):
    name = forms.CharField(required=False)
    realisateur = forms.CharField(required=False)

class Creationcd(forms.Form):
    name = forms.CharField(required=False)
    artiste = forms.CharField(required=False)
    disponible = forms.BooleanField(required=False)

class Updatecd(forms.Form):
    name = forms.CharField(required=False)
    artiste = forms.CharField(required=False)

class Ajoutplateau(forms.Form):
    name = forms.CharField(required=False)
    createur = forms.CharField(required=False)


class AjoutEmprunteurForm(forms.Form):
    name = forms.CharField(max_length=100)
    bloque = forms.BooleanField(required=False)


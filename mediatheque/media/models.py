from django.db import models
from django.db.models.functions import Now


class Media(models.Model):
    name = models.CharField(max_length=255)
    date_emprunt = models.DateField(db_default=Now())
    disponible = models.BooleanField(default=False)
    emprunteur = models.ForeignKey("Emprunteur", on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class Livre(Media):
    auteur = models.CharField(max_length=255)

class Cd(Media):
    artiste = models.CharField(max_length=255)

class Dvd(Media):
    realisateur = models.CharField(max_length=255)

class Emprunteur(models.Model):
    name = models.CharField(max_length=255)
    bloque = models.BooleanField(default=False)

class Jeudeplateau(models.Model):
    name = models.CharField(max_length=255)
    createur = models.CharField(max_length=255)